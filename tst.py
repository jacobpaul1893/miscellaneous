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


df = pd.read_csv("tst.txt", sep=" ", header=None)

print(df)
l1 = df[0].to_list()
l2 = df[1].to_list()
l3 = df[2].to_list()

for i in range(len(l3)):
        if l3[i] == "in":
            l3[i] = durn_live(l2[i])
        elif l3[i].startswith("("):
            l3[i] = l3[i][1:-1]

print(l3)


res = defaultdict(list)

for i, j in zip(l1, l3):
    res[i].append(j)

print(res)

x=list(res.keys())
print(x)
y = list(res.values())
print(y)

td = []
for i in res.values():
    total = 0
    for j in i:
        it = time_in_min(j)
        total += it
    hr = total//60
    min = total%60
    td.append("{0:02d}:{1:02d}".format(hr, min))

dn = list(zip(x, td))
print(dn)

df1 = pd.DataFrame(dn, columns=['Username', "Duration_Worked"])
print(df1)
