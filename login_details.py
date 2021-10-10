import pandas as pd

def space_rm_last(file):
    r = open(file, "r")
    w = open("{0}_n.txt".format(file), "w") 
    for i in r.readlines():
        if i.startswith("reboot"):
            continue
        else:
            w.write(" ".join(i.split()))
            w.write("\n")
    r.close()
    w.close()
    return "{0}_n.txt".format(file)

def filter(file, cols, param):
    cols_to_use = cols
    df = pd.read_csv(space_rm_last(file), sep=" ", header=None, usecols=cols_to_use)
    df.columns = ['Username', 'Month', 'Day', 'Time', 'Year']
    
    df['S.No'] = df.index
    df.set_index('S.No', inplace=True)
    df[param] = df['Month'].astype(str) + ' ' + df['Day'].astype(str) + ' ' + df['Time'].astype(str) + ' ' + df['Year'].astype(str) 
    df = df[['Username', param]]
    #df_csv = df.to_csv(r'Log_frm_last.csv', index="S.No", header=True)
    print(df)

cols_first = [0, 3, 4, 5, 6]
cols_last = [0, 9, 10, 11, 12]
param_first = "First_Login"
param_last = "Last_Logout"

filter("last_logout.txt", cols_last, param_last)

