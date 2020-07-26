print("Welcome to the Even odd number sorter app\n")



while True :
    l = list(map(int,input("Enter in a string of numbers seperated by commas : ").split(",")))
    #print(l)

    even = []
    odd = []



    print("---- Result Summary ----")
    for i in l :
        if i%2 == 0 :
            print("{} is even.".format(i))
            even.append(i)
        else :
            print("{} is odd.".format(i))
            odd.append(i)


    even.sort()
    odd.sort()

    print("\nThe following numbers are even: ")
    for i in even :
        print("\t\t"+str(i))

    print("\nThe following numbers are odd :")
    for i in odd :
        print("\t\t"+str(i))
    
    boole = input("Would you like to run the program again : ")
    if boole == 'y' :
        continue
    else :
        break