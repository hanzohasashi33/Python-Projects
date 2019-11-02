import webbrowser

import requests
from bs4 import BeautifulSoup

'''
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
'''



input_func = None
try:
    input_func = raw_input('Enter the song to be played: ')
except NameError:
    input_func = input('Enter the song to be played: ')


'''
Basic Syntax : 
 try:
    // Code
 except:
    // Code
How try() works?

First try clause is executed i.e. the code between try and except clause.
If there is no exception, then only try clause will run, except clause is finished.
If any exception occured, try clause will be skipped and except clause will run.
If any exception occurs, but the except clause within the code doesn't handle it, it is passed on to the outer try statements. If the exception left unhandled, then the execution stops.
A try statement can have more than one except clause
'''

query = input_func.replace(' ', '+')

# search for the best similar matching video
url = 'https://www.youtube.com/results?search_query=' + query       #see in your search bar to get a clearer idea
source_code = requests.get(url, timeout=15)

'''
The GET Request
HTTP methods such as GET and POST, determine which action you're trying to perform when making an HTTP request. Besides GET and POST, there are several other common methods that you'll use later in this tutorial.

One of the most common HTTP methods is GET. The GET method indicates that you're trying to get or retrieve data from a specified resource. To make a GET request, invoke requests.get().


The Response
A Response is a powerful object for inspecting the results of the request. Let's make that same request again, but this time store the return value in a variable so that you can get a closer look at its attributes and behaviors.
'''


plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

# fetches the url of the video
songs = soup.findAll('div', {'class': 'yt-lockup-video'})
i = input("input the n th number of search song you want to see : ")
song = songs[i].contents[0].contents[0].contents[0]
# link = song['href']
# webbrowser.open('https://www.youtube.com' + link)

try:
    link = song['href']
    webbrowser.open('https://www.youtube.com' + link)
except KeyError:
    print("Can't find any song,check your network or try a new word")

