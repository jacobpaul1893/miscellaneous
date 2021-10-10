import pandas as pd
from functools import reduce

def conv_df(file, column):
    df = pd.read_csv(file, header=None)
    df.columns = [ column]
    df['S.No'] = df.index
    df.set_index('S.No', inplace=True)
    return df

df1 = conv_df("x1", "Username")
df2 = conv_df("x2", "First Login")
df3 = conv_df("x3", "Last Logout")
df4 = conv_df("x4", "Duration")


frames = [df1, df2, df3, df4]

df_final = reduce(lambda  left,right: pd.merge(left,right,on=['S.No'], how='outer'), frames)
print(df_final)
df.to_csv(r'Login_data.csv', index="S.No", header=True)
