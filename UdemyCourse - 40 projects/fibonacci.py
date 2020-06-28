def fibonacci(num) :
    if num == 1 :
        return 1 
    elif num == 2 :
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

print("Welcome to the fibonacci app\n")
num = int(input("Enter number upto you want the fibonacci app : "))
for i in range(1,num+1) :
    print(fibonacci(i))


print("\nThe corresponding Golden Ratio values are : ")
for i in range(2,num+1) :
    print(fibonacci(i)/fibonacci(i-1))