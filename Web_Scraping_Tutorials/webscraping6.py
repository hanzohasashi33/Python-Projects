from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#TREE NAVIGATION USING BS$4


html = urlopen("https://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"lxml")




'''
for child in bsObj.find("table",{"id": "giftList"}).children :                 #to print all children classes
    print(child)

for child in bsObj.find("table",{"id": "giftList"}).descendants :              #to print all descendent classes
    print(child)

for sibling in bsObj.find("table",{"id" : "giftList"}).tr.next_siblings :       #siblings will only call next siblings
    print(sibling)
'''


print(bsObj.find("img",{"src" : "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
