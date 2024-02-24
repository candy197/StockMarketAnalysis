from bs4 import BeautifulSoup
import requests as rt
from tqdm import tqdm
import sqlite3
import os 
import pandas as pd



Path = os.getcwd()+"/Offline_Db/"
con_obj = sqlite3.connect(Path+"Sector.db")
con_obj2 = sqlite3.connect(Path+"StockData.db")
def SectorExtractor(name):
    newName = name.replace(" ","-").replace("&","").replace("--","-").replace("--","-")
    URL ="https://www.moneycontrol.com/india/stockmarket/sector-classification/marketstatistics/nse/"+newName+".html"
    page = rt.get(URL)#URL Request 
    StatusOfUrl = page.status_code #Checking Modified Site is working fine or not
    if(StatusOfUrl != 200):
        print(URL+" = "+ StatusOfUrl)
    else:
        queryname = newName.replace("-","_").capitalize()        
        query = "CREATE TABLE if not exists {}(SYMBOL varchar(255),Company Name varchar(25),Industry varchar(255),HIGH numeric(255),LOW numeric(255))".format(queryname)
        table = (query)
        con_obj.execute(table)
        CreateTable(newName)

def CreateTable(newName):
    URL = "https://www.moneycontrol.com/india/stockmarket/sector-classification/marketstatistics/nse/"+newName+".html"
    page = rt.get(URL)
    src = page.content
    soup = BeautifulSoup(src,'lxml')
    table = soup.find("table")
    rows = soup.findAll("tr")
    data = []
    for row in rows:
        cells = row.find_all("td")
        row_data = []
        for cell in cells:
            row_data.append(cell.text.strip())
        data.append(row_data)

    df = pd.DataFrame(data)
    df.columns=("Company Name","Industry","Last Price","Change","Change %","Market Cap")             
    for name in df["Company Name"]:
     if  name != None and len(name) != 0:
        queryname = name.replace("-","_").replace(" ","_").replace("(","_").replace(")","_").replace(".","").replace("&","And").replace("3","").replace("60","").replace("5","").capitalize()       
        query = "CREATE TABLE if not exists {}(SYMBOL varchar(255),Company Name varchar(25),Industry varchar(255),HIGH numeric(255),LOW numeric(255))".format(str(queryname))
        print(query)        
        con_obj.execute(query)


page = rt.get("https://www.moneycontrol.com/india/stockmarket/sector-classification/marketstatistics/nse/agri.html")
src = page.content
soup = BeautifulSoup(src,'lxml')
Sector_name = soup.find("div",attrs={"class":"lftmenu"})
href_tags = Sector_name.find_all('a', href=True)
with tqdm(total=len(href_tags),desc="Creating Tables") as pbar:
    for i in href_tags:
        name = i.text
        SectorExtractor(name.lower())
        pbar.update(1)
print("Completed Successfully")