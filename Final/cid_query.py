# -*- coding: utf-8 -*-
import csv

#課號
def DBcid(cid:int):
    with open("Index/MyDB_cid_tree.csv","r") as f:
        data = csv.reader(f)
        total_index = None
        for i,row in enumerate(data,1):
            if i == 1:
                for j in range(1,len(row),2):  #從根節點的最左邊開始（每次加二找子節點的index）
                    if int(row[j]) > cid:       #當目前索引大於我要的就跳前一個指向的葉節點
                        index=int(row[j-1])
                        break
                    if j == len(row)-2:         #當是大於根節點的最後一個索引值就跳最後一個葉節點
                        index=int(row[j+1])
                        break
            if i == index:                      #跑到對應的行數
                for j in range(0,len(row),2):   
                    if int(row[j])== cid:       #找到對的值
                        total_index=int(row[j+1])
                        break
    
    if total_index == None:    #對比失敗
        print("查無此課號")
        return
    
    with open("Data/MyDB_data_cid.csv","r",encoding='utf-8') as f:
        data= csv.reader(f)
        for i,row in enumerate(data,1):     #把資料index化
            if i == total_index:
                current_cid=row[0]      #把目前課號設成第一個的索引課號
                print(row[2])
            elif i > total_index :
                if row[0]==current_cid:
                    print(row[2])
                else:
                    break