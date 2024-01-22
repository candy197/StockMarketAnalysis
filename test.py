from bs4 import BeautifulSoup
import requests as rt



page = rt.get("https://www.moneycontrol.com/india/stockmarket/sector-classification/marketstatistics/nse/agri.html")

src = page.content
soup = BeautifulSoup(src,'lxml')
Sector_name = soup.find("div",attrs={"class":"lftmenu"})
href_tags = Sector_name.find_all('a', href=True)
for i in href_tags:
    print(i.text)
