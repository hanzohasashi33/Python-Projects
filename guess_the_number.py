import random
from collections import OrderedDict


def play_game(isPlaying,number_of_attempts) : 
    play_again = input("Do you want to play again ? : ")
    if play_again == 'y' or play_again == 'Y' or play_again == "YES" or play_again == "yes" or play_again == "Yes" :
        number_of_attempts += 1 
        isPlaying = True 
    elif play_again == "N" or play_again == "n" or play_again == "NO" or play_again == "no" or play_again == "No" :
        isPlaying = False 
    else :
        print ("Please enter proper input : ")
        play_game(isPlaying,number_of_attempts)
    
    return isPlaying,number_of_attempts 

def game() : 
    number_of_attempts = 1
    score = 0
    isPlaying = True 
    score_of_player = 0

    while isPlaying == True :
        print ("Choose the range of the number you want to guess",end = " : ")
        left_range = int(input())
        print ("The higher the number is - more the chance of getting a high score.")

        guess_number = random.randint(0,left_range)
        input_number = int(input())

        if input_number == guess_number : 
            print ("You have Guessed correctly")
            print ("The probability of you guessing this number is : " + str(1/float(left_range)))
            score += left_range
            print("Your score is : %d" %(score))


        else : 
            if guess_number > input_number :
                diff = guess_number - input_number
            else :
                diff = input_number - guess_number
            print("You have missed the number by %d "%(diff)) 

        
        boole,attempts = play_game(isPlaying,number_of_attempts)
        if(boole == False ) :
            break 
             
    print ("Game over !")
    print ("Well Played")
    finalscore = score / attempts 
    score_of_player = finalscore
    return score_of_player

if __name__ == "__main__" : 
    score_of_player = game ()
    player_name=str(input("Enter your name: "))               #For Leaderboard
    file = open('leaderboard.txt','a')                        #Append mode as of now.
    file.write('\n' + player_name +' ' + (score_of_player))
    file.close()

    dictionary = {}
    names = []
    scores = []
    with open("leaderboard.txt") as f:
        for line in f:
            (key, val) = line.split()
            dictionary[key] = val
            names.append(key)
            scores.append(val)
            
    print ("--------------------------------------------------------------------------")
    print ("The leaderboard is : ")
    a1_sorted_keys = sorted(dictionary, key=dictionary.get, reverse=True)
    for r in a1_sorted_keys:
        print(r, dictionary[r])