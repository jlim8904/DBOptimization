# -*- coding: utf-8 -*-
import csv

#課號
def DBcname(keyword:str):
    with open("Index/MyDB_cname.csv","r",encoding='utf-8') as f:
        data = csv.reader(f)
        index = None            #初始化index
        for row in data:
            if row[0].upper() == keyword.upper():  #將大小寫統一再進行對比
                index = row[1].split(',')   #將所有課名的索引（不同課號）分開
                break
            
    if index == None :          #對比失敗
        print("查無此課程或輸入錯誤")
        return
            
    #Course_ID為主鍵
    
    with open("Data/MyDB_data_cid.csv","r",encoding='utf-8') as f:
        data = csv.reader(f)
        second_index = 0    #目前索引
        for i,row in enumerate(data,1):
            if i == int(index[second_index]):
                input("課程 " + row[0] + ':')
                current_cid = row[0]
                print(row[2])
            elif i > int(index[second_index]):
                if row[0] == current_cid:   #看當前的課號是否和要的一致
                    print(row[2])
                elif second_index + 1 < len(index):  #是否不是最後一個index
                    second_index += 1       #目前索引加一
                else:
                    break