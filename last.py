import pandas as pd

r = open("last.txt", "r")
w = open("last_n.txt", "w") 
for i in r.readlines():
    if i.startswith("reboot"):
        continue
    else:
        w.write(" ".join(i.split()))
        w.write("\n")
r.close()
w.close()

cols_to_use = [0, 3, 4, 5, 7, 8]
df = pd.read_csv('last_n.txt', sep=" ", header=None, usecols=cols_to_use)
df.columns = ['Username', 'Month', 'Day', 'Login', 'Logout', 'Duration']
df['S.No'] = df.index
df = df.drop(df.index[-1])
df.set_index('S.No', inplace=True)
df['Login_Time'] = df['Month'].astype(str) + ' ' + df['Day'].astype(str) + ' ' + df['Login'] 
df = df[['Username', 'Login_Time', 'Logout', 'Duration']]
#df_csv = df.to_csv(r'Log_frm_last.csv', index="S.No", header=True)
print(df)
