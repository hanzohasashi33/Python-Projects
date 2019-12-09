#REGEX EXPRESSIONS  

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re 


html = urlopen("https://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"lxml")

images = bsObj.find_all("img" , {"src" : re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for img in images : 
    print(img["src"])