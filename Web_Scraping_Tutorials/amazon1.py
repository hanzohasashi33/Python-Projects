import requests 
from bs4 import BeautifulSoup
import smtplib



'''
The User-Agent request header is a characteristic string
that lets servers and network peers identify the application, 
operating system, vendor, and/or version of the requesting user agent.
'''
headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}


def checkprice(url,budget) : 
    page = requests.get(url, headers = headers)
    bsObj = BeautifulSoup(page.content,"html.parser")

    #print (bsObj.prettify())

    title = bsObj.find(id = "productTitle").get_text()
    price = bsObj.find(id = "priceblock_ourprice").get_text()
    converted_price = price[2:-3]

    l=[]
    for i in converted_price:
        if(i!='.' and i!=','):
            l.append(int(i))
    string=''
    for i in l:
        string+=str(i)
    final_price=int(string)

    if final_price<budget:
        print(title.strip())
        print (price)
        
    else:
        print(title.strip(),"is over your budget of",str(budget))
        print ("The current status is :")
        print(title.strip())
        print (price)

if __name__ == "__main__":
    url = input("")
    budget = int(input())
    checkprice(url,budget)