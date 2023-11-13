import csv
from myhash import hash

with open("backup/MyDB_sid_fmt1.csv", newline='') as f:
    rows = csv.reader(f)
    d = list(rows)

del d[0]
data = d

with open("backup/MyDB_sid_fmt2.csv", newline='') as f:
    rows = csv.reader(f)
    d = list(rows)

del d[0]
data += d

num = []

sid = [None] * 1000

for i,x in enumerate(data):
    num.append(hash(str(x[0]),1000))
    if i == 0:
        print(num,x)

for i,x in enumerate(data):
    if sid[num[i]] == None:
        sid[num[i]]=x
    else:
        sid[num[i]].append(x[0])
        sid[num[i]].append(x[1])

with open("Index/MyDB_sid.csv", 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(sid)