from urllib.request import urlopen 
from urllib.error import HTTPError

try :
    html = urlopen("http://www.pythonscrping.com/pages/page1.html")

except Exception as e :
    print("The page is not found")
    print("URL was mistyped")


else :
    #continue
    print("It works !!!")