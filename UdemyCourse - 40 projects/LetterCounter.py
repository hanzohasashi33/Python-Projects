# Basic Data types challenge - 1 : letter counter program

#greeter
print("Welcome to the letter counter app")

#user input
name = input('Enter your name : ')
print("Hello",name)
print("Enter the message and corresponding letter you want to count")
msg = input('Enter your message : ')
char = input('Enter the letter : ')

#standardize to lower case 
msg = msg.lower()
char = char.lower()

#count characters
count = 0
for i in msg :
    if i == char :
        count += 1
    
#print output
print("{},your msg has {}'s {} in it".format(name,count,char))
