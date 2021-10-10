import pandas as pd
from datetime import datetime
from collections import defaultdict

def time_in_min(time):
    tm = 0
    t1 = [int(m) for m in time.split(':')]
    tm += (t1[0] * 60 + t1[1])
    return tm

def durn_live(intime):
    c_time = datetime.now().strftime("%H:%M")
    im = time_in_min(intime)
    cm = time_in_min(c_time)
    tot_min = cm - im
    hr = tot_min//60
    min = tot_min%60
    return "{0:02d}:{1:02d}".format(hr, min)

def conv_df(file, column):
    """ Function to convert text file to pandas dataframe
    Takes file & the column as input.
    Here the first line read the text file as csv by 
    providing space as seperator and avoiding headers
    In 2nd line we choose the column names required,
    1st column defined as Username by default and the
    2nd column changes according to the file, so given as 
    a variable called column. Now the 3rd line returns
    the final dataframe"""

    df = pd.read_csv(file, sep=" ", header=None)
    df.columns = ['Username', column]
    return df


df_fl = conv_df('first_login.txt', 'First Login') # Creating dataframe for First login
df_ll = conv_df('last_logout.txt', 'Last Logout') # Creating df for Last logout

df_tmp = pd.read_csv("dn.txt", sep=" ", header=None)

l1 = df_tmp[0].to_list()
l2 = df_tmp[1].to_list()
l3 = df_tmp[2].to_list()

for i in range(len(l3)):
    if l3[i] == "in":
        l3[i] = durn_live(l2[i])
    elif l3[i].startswith("("):
        l3[i] = l3[i][1:-1]


dn_dict = defaultdict(list)

for i, j in zip(l1, l3):
    dn_dict[i].append(j)


user_list=list(dn_dict.keys())

td = []
for i in dn_dict.values():
    total = 0
    for j in i:
        it = time_in_min(j)
        total += it
    hr = total//60
    min = total%60
    td.append("{0:02d}:{1:02d}".format(hr, min))

dn = list(zip(user_list, td))

df_dn = pd.DataFrame(dn, columns=['Username', "Duration Worked"])


df = df_fl.merge(df_ll, on='Username').merge(df_dn, on='Username') # Merging all 3 df on the column Username
df['S.No'] = df.index # Creating S.No column with df index as the contents
df.set_index('S.No', inplace=True) # Making S.No column as the Index of df
df.to_csv(r'Today_Login.csv', index="S.No", header=True) # Converting the df to csv with index as S.No & including Header
