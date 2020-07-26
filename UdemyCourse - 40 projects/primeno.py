from math import sqrt,ceil
import time


def primenum(num) :
    count = 0 
    for i in range(1,ceil(sqrt(num))+1) :
        if num%i == 0 :
            count += 1
        if count > 1 :
            return -1
    return 1 



print("Welcome to the Prime Number App\n")


while True : 
    print("Enter 1 to determine if a specific number is prime : ")
    print("Enter 2 to determine all prime numbers within a set range : ")
    choice = int(input("Enter your choice 1 or 2 : "))


    if choice == 1 :
        num = int(input("Enter a number : "))
        if primenum(num) == 1 :
            print("{} is prime!".format(num))
        else :
            print("{} is not prime!".format(num))

    else :
        lower = int(input("Enter the lower bound : "))
        upper = int(input("Enter the upper bound : "))
        print("The following numbers between {} and {} are prime : ".format(lower,upper))
        start_time = time.time()
        input("Press enter to continue.")
        for i in range(lower,upper+1) :
            if primenum(i) == 1 :
                print(i)
        end_time = time.time()
        print("It took {}s".format(round(end_time-start_time,4)))
    boole = input("Would you like to run the program again : ")
    if boole == 'y' :
        continue
    else :
        print("Thanks for using the program.")
        break