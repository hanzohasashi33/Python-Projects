from bs4 import BeautifulSoup
from datetime import datetime 
import requests 
import urllib.request 


res = requests.get('https://bing.wallpaper.pics/')
soup = BeautifulSoup(res.text,"lxml")


image_box = soup.find("a",{"class" : "cursor_zoom"})
image = image_box.find('img')
link = image['src']
#print(link)


#urllib.request.urlretrieve(link,'_new.jpg_')
filename = datetime.now().strftime('%d-%m-%y')
urllib.request.urlretrieve(link,filename)
