from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import csv

start_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
browser = webdriver.Chrome('./chromedriver')

browser.get(start_url)

time.sleep(10)

def scrap():
    bsoup = BeautifulSoup(browser.page_source, 'html.parser')
    dwarf_table = bsoup.find_all('table',attrs={'class':'wikitable sortable jquery-tablesorter'})
    temp_list=[]
    table_rows = dwarf_table[1].find_all('tr')
    for tr in table_rows:
        data_tags = tr.find_all('td')
        r = [i.text.rstrip( ) for i in data_tags]
        temp_list.append(r)
    name_list=[] 
    dist_list=[]
    mass_list=[]
    radius_list=[]
    #problem starts here
    print(temp_list[1])
    for i in range(1, len(temp_list)):
        name_list.append(temp_list[i][0])
    for i in range(1, len(temp_list)):
        dist_list.append(temp_list[i][5])
    for i in range(1, len(temp_list)):
        mass_list.append(temp_list[i][7])
    for i in range(1, len(temp_list)):
        radius_list.append(temp_list[i][8])
    #problem ends here
        
    #with open('stars.csv', "w") as f:
    #    cw = csv.writer(f)   
    #    cw.writerow(['names','distance','mass','radius'])'names','distance','mass','radius'
    #    cw.writerows(name_list)
    #    cw.writerows(dist_list)
    #    cw.writerows(mass_list)
    #    cw.writerows(radius_list)
    df = pd.DataFrame(list(zip(name_list,dist_list,mass_list,radius_list)), columns=['names','distance','mass','radius'])
    print(df)
    df.to_csv('teststars.csv')        
        

scrap()