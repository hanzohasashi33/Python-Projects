import requests
from bs4 import BeautifulSoup
import csv


#get the response from url and create a soup object
name = input("Enter your name : ")
print("Hi",name)

while(True) :
    print("Select one of the following categories : ")
    print("1.Animal Jokes")
    print("2.Food Jokes")
    print("3.Clean Jokes")
    print("4.Family Jokes")
    print("5.National Jokes")
    print("6.Office Jokes")
    print("7.Political Jokes")
    print("0.exit")
    
    url = ""
    flag = 1
    option = int(input("Select one of the categories : "))

    if option == 0 :
        break 
    elif option == 1:
        url = "http://www.laughfactory.com/jokes/" + "animal-jokes"
        csv_file = open('jokescraper-animaljokes.csv','w')
    elif option == 2 :
        url = "http://www.laughfactory.com/jokes/" + "food-jokes"
        csv_file = open('jokescraper-food.csv','w')
    elif option == 3 :
        url = "http://www.laughfactory.com/jokes/" + "clean-jokes"
        csv_file = open('jokescraper-cleanjokes.csv','w')
    elif option == 4 :
        url = "http://www.laughfactory.com/jokes/" + "family-jokes"
        csv_file = open('jokescraper-familyjokes.csv','w')
    elif option == 5 :
        url = "http://www.laughfactory.com/jokes/" + "national-jokes"
        csv_file = open('jokescraper-nationaljokes.csv','w')
    elif option == 6 :
        url = "http://www.laughfactory.com/jokes/" + "office-jokes"
        csv_file = open('jokescraper-officejokes.csv','w')
    elif option == 7 :
        url = "http://www.laughfactory.com/jokes/" + "political-jokes"
        csv_file = open('jokescraper-politicaljokes.csv','w')
    else :
        print("Invalid option")
        flag = 0

    if flag == 1 :
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['S.no'," ",'Joke'])
        j = 1 
        i = 1
        html = requests.get(url).text
        soup = BeautifulSoup(html,'lxml')
        all_jokes = soup.find_all("div",class_ = "joke-text") 

        for joke in all_jokes :
            joke_text = joke.p.text.lstrip().rstrip() 
            print(joke_text)
            csv_writer.writerow([i," ",joke_text])
            print()
            i += 1
    
        csv_file.close()
