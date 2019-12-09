from urllib.request import urlopen 
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page1.html")
#print(bsObj.h1)                #prints the header file
# print(bsObj.div)
# print(bsObj.title)

try :
    bsObj = BeautifulSoup(html.read(),'lxml')
    #badContent = bsObj.nonexistingtagg.anotherTag
    badContent = bsObj.head

except Exception as e :
    print("Tag does not exist")

else :
    if badContent == None :
        print("It does not contain anything")
        print("tag does not exist")
    else :
        print(badContent)