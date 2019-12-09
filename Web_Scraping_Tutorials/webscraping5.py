from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")
bsObject = BeautifulSoup(html,'lxml')

namelist = bsObject.find_all("",{"id" : "text"})
for name in namelist :
    print(name.get_text())