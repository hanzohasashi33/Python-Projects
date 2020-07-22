from math import sqrt,ceil

print("Welcome to the factor generator app\n")

while(True) :
    num = int(input("Enter a number to determin all factors of the number : "))
    factors = []
    i = 1
    while(i <= ceil(sqrt(num))) :
        if num%i == 0 :
            factors.append(i)
        i += 1

    print("\nIn summary : ")
    for i in factors :
        print("{} * {} = {}".format(int(i),int(num/i),int(i*num/i)))

    boole = input("Run again(y/n) : ")
    if boole == 'n' :
        break 