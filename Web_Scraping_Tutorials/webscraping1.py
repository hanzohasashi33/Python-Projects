from urllib.request import urlopen 

html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())


#this code outputs the entire html page rather than the contents.
#output looks like a html code 
#as compared to content
