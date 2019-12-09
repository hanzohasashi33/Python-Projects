from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")

bsObj = BeautifulSoup(html,"lxml")                      #creates a bsObject
namelist = bsObj.findAll("span",{"class" : "green"})    #here it finds all objects with tag   <span class = green >

for name in namelist :
    print(name.get_text())               #get_text() removes the tag of the html elements
    print(name)                          #prints the name with tag