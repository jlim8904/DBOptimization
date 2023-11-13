# -*- coding: utf-8 -*-
from cid_query import DBcid
from cname_query import DBcname
from sid_query import DBsid

Flag = True
while(Flag):
    keywords = input("請輸入欲查詢之資料，0為結束：").split(',')
    for i,keyword in enumerate(keywords,1):
        if keyword == '0':
            Flag = False
            break
        elif keyword == '':
            continue
        elif len(keywords) > 1:
            input("顯示第" + str(i) + "筆，" + keyword + "的資料：")
            
        if len(keyword) == 4 and keyword.isdigit():
            DBcid(int(keyword))
        elif (len(keyword) == 8 or len(keyword) == 10) and keyword[0].upper() == 'D' and keyword[1:].isdigit():
            DBsid(keyword.upper())
        else:
            DBcname(keyword)