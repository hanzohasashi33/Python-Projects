Rock Paper Scissor game
import random


def game(user,comp) :
    if user == 'rock' and comp == 'paper' :
        print("computer wins")
        return 0,1
    
    elif user == 'rock' and comp == 'scissors' :
        print("user wins")
        return 1,0
    
    elif user == 'rock' and comp == 'rock' :
        print("Match Draw")
        return 0,0
    
    elif user == 'paper' and comp == 'rock' :
        print("user wins")
        return 1,0
    
    elif user == 'paper' and comp == 'scissors' :
        print("computer wins")
        return 0,1
    
    elif user == 'paper' and comp == 'paper' :
        print("Match draw")
        return 0,0
    
    elif user == 'scissors' and comp == 'paper' :
        print("User wins")
        return 1,0
    
    elif user == 'scissors' and comp == 'rock' :
        print("computer wins")
        return 0,1
    
    elif user == 'scissors' and comp == 'scissors' :
        print("Match Draw")
        return 0,0
    
    else :
        print("Invalid Input")
        return 0,0


isRunning = True 
user_score = 0
computer_score = 0
while isRunning == True :
    start = input("Do You want to start the game :")
    if start == 'y' or start == 'Y' or start == 'YES' or start == 'Yes' or start == 'yes':
        l = ['rock','paper','scissors']
        comp_choice = random.choice(l)
        #print (comp_choice)
        user_choice = input("Enter Your Choice : ")
        user_choice = user_choice.lower()
        print("The Choice Of computer is : " + comp_choice)
        user_s,computer_s = game(user_choice,comp_choice)
        user_score += user_s
        computer_score += computer_s
        #print(user_score)
        #print(computer_score)

        
    else :
        isRunning = False
        print("Final score of user is : " + str(user_score))
        print("Final score of computer is : " + str(computer_score))
        if user_score > computer_score :
            print("user wins")
        elif user_score < computer_score :
            print("computer wins")
        else :
            print("match draw")
