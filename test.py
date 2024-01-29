from bs4 import BeautifulSoup
import requests as rt
from tqdm import tqdm
import sqlite3
import os 



Path = os.getcwd()+"/Offline_Db/"
print(Path)
con_obj = sqlite3.connect(Path+"StockData.db")
def tableExtractor(name):
    newName = name.replace(" ","-").replace("&","").replace("--","-").replace("--","-")
    URL ="https://www.moneycontrol.com/india/stockmarket/sector-classification/marketstatistics/nse/"+newName+".html"
    page = rt.get(URL)#URL Request 
    StatusOfUrl = page.status_code #Checking Modified Site is working fine or not
    if(StatusOfUrl != 200):
        print(URL+" = "+ StatusOfUrl)
    else:
        queryname = newName.replace("-","_")        
        query = "CREATE TABLE if not exists {}(SYMBOL varchar(255),Name varchar(25),HIGH numeric(255),LOW numeric(255),W52_HIGH numeric(255),W52_LOW numeric(255))".format(queryname)
        table = (query)
        con_obj.execute(table)

def Push_Data():
    pass  
    

   
    
page = rt.get("https://www.moneycontrol.com/india/stockmarket/sector-classification/marketstatistics/nse/agri.html")

src = page.content
soup = BeautifulSoup(src,'lxml')
Sector_name = soup.find("div",attrs={"class":"lftmenu"})
href_tags = Sector_name.find_all('a', href=True)
with tqdm(total=len(href_tags),desc="Checking Site Health") as pbar:
    for i in href_tags:
        name = i.text
        tableExtractor(name.lower())
        pbar.update(1)
print("Completed Successfully")



