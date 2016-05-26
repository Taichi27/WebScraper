# coding: utf-8

from bs4 import BeautifulSoup
import urllib.request
import csv
import glob
import re
import datetime
import os
import time


#file_list = glob.glob('./*/*/*.html')
file_list = glob.glob('nursery_school/*/*/*.html')
today = str(datetime.date.today())
replace_today = today.replace("-","")
filename = "/analytics-data/nursery_school/"+replace_today+"nursery_school_html"+"/csv_data.csv"
f = open(filename,'w',encoding='cp932',errors='replace')
writer = csv.writer(f,lineterminator='\n')
writer.writerow(['No','施設名','住所','施設詳細'])
print(file_list)


address_list = []
count = 1


for htmlfile in file_list:
    table_list = []
    time.sleep(1)
    soup = BeautifulSoup(open(htmlfile,'r',encoding="shift-jis",errors="replace"))


    for item in soup.find_all('table',attrs={"class":"s-table"}):
        table_list.append(item)
        print(table_list)


    contents_num = len(table_list)



    for mal in range(contents_num):
        info = table_list.pop(0)


        for nursery_name in info.find_all("th",attrs={"colspan":"6"}):
            true_nursery_name = nursery_name.text


        for pre_nursery_address in info.find_all("td",attrs={"class":"address t-left"}):
            print(pre_nursery_address)
            nursery_address = pre_nursery_address.text
            print(nursery_address)


        detail_icon_list = []


        for pre_icon in info.find_all("td",attrs={"width":"140"}):


            for pre_2_icon in pre_icon.find_all("img"):
                detail_icon = pre_2_icon["alt"]
                detail_icon_list.append(detail_icon)


                while detail_icon_list.count("")>0:
                    detail_icon_list.remove("")


            csv_list =[str(count),true_nursery_name,nursery_address]
            writer.writerow(csv_list+detail_icon_list)
            count += 1
