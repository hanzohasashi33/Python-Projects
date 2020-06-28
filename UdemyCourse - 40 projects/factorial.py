def factorial(num) :
    fact = 1
    for i in range(1,num+1) :
        fact *= i
    return fact 



if __name__ == "__main__":
    print("Welcome to the Factorial app")
    n = int(input("\nWhat number would you like to compute the factorial of ? "))
    msg = ""
    for i in range(1,n+1) :
        if i == n :
            msg += str(i)
        else :
            msg = msg + str(i) + "*"

    print("{}! = {}".format(n,msg))
    print("The factorial is {}".format(factorial(n)))