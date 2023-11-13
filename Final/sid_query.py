# -*- coding: utf-8 -*-
import csv
from myhash import hash

#學號
def DBsid(sid:str):
    index = hash(sid,1000)
    # print(index)#886行
    with open("Index\MyDB_sid.csv","r",encoding='UTF-8') as f:
        data = f.readlines()[index:index+1]
        data = list(data)
        data = (data[0].split(','))#用逗號去分割
        data[len(data)-1] = data[len(data)-1][:-1]#把最後一個處理掉
        # print(data)#輸出對應行數的值
        # for i,nums in enumerate(data):
        #     if nums == sid:
        #         print(i)
        for i in range(0,len(data),2):
            if data[i] == sid:
                number = int(data[i+1])
        # print(number)#行數
    with open("Data\MyDB_data_sid.csv","r",encoding='UTF-8') as g:
        data_1 = csv.reader(g)
        for i,row in enumerate(data_1):
            if i == number-1:
                print(row[1],row[2])
                row_sid = row[0]
            elif i > number-1:
                if row_sid == row[0]:
                    print(row[1],row[2])
                else:
                    break


# #課號
# def DBsid(sid:str):
#     index = hash(sid,1000)
#     with open("Index/MyDB_sid.csv","r") as f:
#         data = csv.reader(f)
#         total_index = None
#         for i,row in enumerate(data):
#             if i == index:                      
#                 for j in range(0,len(row),2):
#                     if row[j] == sid:       
#                         total_index=int(row[j+1])
#                         break
    
#     if total_index == None:  
#         print("查無此學號")
#         return
    
#     with open("Data/MyDB_data_sid.csv","r",encoding='utf-8') as f:
#         data= csv.reader(f)
#         for i,row in enumerate(data,1):   
#             if i == total_index:
#                 current_sid=row[0]    
#                 print(row[1],row[2])
#             elif i > total_index :
#                 if row[0]==current_sid:
#                     print(row[1],row[2])
#                 else:
#                     break