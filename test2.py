from bs4 import BeautifulSoup
import requests as rt
from tqdm import tqdm
import sqlite3
import os 
import pandas as pd


Path = os.getcwd()+"/Offline_Db/"
con_obj = sqlite3.connect(Path+"StockData.db")

page = rt.get("https://www.moneycontrol.com/india/stockmarket/sector-classification/marketstatistics/nse/agri.html")

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


df.to_csv("test.csv")

print(df)