print("Welcome to the Multiplication/Exponent Table App\n")

name = input('Hello,What is your name : ')
name = name.strip()

num = float(input("What number would you like to worl with : "))
print("\n")
print("Multiplication table for {}".format(num))
print("\n")
for i in range(1,10) :
    print("\t{} * {} = {}".format(float(i),num,round(num*i,4)))

print("\nExponent Table for {}".format(num))
for i in range(1,10) :
    print("\t{} ** {} = {}".format(num,int(i),round(num**i,4)))

print("\n")
msg = name + " math is cool!"
print("{} Math is cool!".format(name))
print(msg.lower().rjust(20))
print(msg.title().rjust(30))
print(msg.upper().rjust(40))