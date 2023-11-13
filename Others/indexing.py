# -*- coding: utf-8 -*-
import csv

#讀取原始檔
with open("backup/原始檔/DB_students_tc_utf8.csv", encoding='utf-8', newline='') as f:
    rows = csv.reader(f)
    data = list(rows)

data[1:] = sorted(data[1:], key=lambda x : x[1])
data[1:] = sorted(data[1:], key=lambda x : x[0])

sid_fmt1 = []
sid_fmt2 = []

for row in data[1:]:
    if len(row[0]) == 8:
        sid_fmt1.append(row[0])
    if len(row[0]) == 10:
        sid_fmt2.append(row[0])

temp = sorted(set(sid_fmt1))
sid_fmt1 = []
for x in temp:
    sid_fmt1.append([x,''])
i = 0
for row_num,row in enumerate(data[1:]):
    if i == len(temp):
        break
    if row[0] == sid_fmt1[i][0] and sid_fmt1[i][1] == '':
        sid_fmt1[i][1] = row_num + 2
        i+=1
        
sid_fmt1.insert(0,['student_id','index'])
with open("Index/MyDB_sid_fmt1.csv", 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(sid_fmt1)  

temp = sorted(set(sid_fmt2))
sid_fmt2 = []
for x in temp:
    sid_fmt2.append([x,''])
i = 0
for row_num,row in enumerate(data[1:]):
    if i == len(temp):
        break
    if row[0] == sid_fmt2[i][0] and sid_fmt2[i][1] == '':
        sid_fmt2[i][1] = row_num + 2
        i+=1
        
sid_fmt2.insert(0,['student_id','index'])
with open("Index/MyDB_sid_fmt2.csv", 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(sid_fmt2)  
    

#主要資料檔整理
with open("Data/MyDB_data_sid.csv", 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerows(data)


#欄位整理
for x in data:
    temp = x[0]
    x[0] = x[1]
    x[1] = x[2]
    x[2] = temp


#各欄位整理 
cid = []
cname = []

data[1:] = sorted(data[1:], key=lambda x : x[0])

for row in data[1:]:
    cname.append(row[1])
    if row[0] not in cid:
        cid.append(row[0])

cname = set(cname)
temp = sorted(cname)
cname = []
for x in temp:
    cname.append([x,''])

 
temp = cid
cid = []
for x in temp:
    cid.append([x,''])
i = 0
for row_num,row in enumerate(data[1:]):
    if i == len(temp):
        break
    if row[0] == cid[i][0] and cid[i][1] == '':
        cid[i][1] = row_num + 2
        i+=1

cid.insert(0,['course_id','index'])
with open("Index/MyDB_cid.csv", 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(cid)  
    

#主要資料檔整理
with open("Data/MyDB_data_cid.csv", 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerows(data)
    
#課名資料索引整理
cid_current = ''
for row_num,row in enumerate(data[1:]):
    if cid_current == row[0]:
        continue
    elif cid_current != row[0]:
        cid_current = row[0]
        for course_name in cname:
            if row[1] == course_name[0]:
                if course_name[1] == '':
                    course_name[1] += str(row_num + 2)
                else:
                    course_name[1] += ',' + str(row_num + 2)
                break
             
             
cname.insert(0,['course_name','index'])       
with open("Index/MyDB_cname.csv", 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerows(cname)
