from datetime import date,time,datetime

print("Welcome to the Grocery List app")
x = datetime.now()
print("Current date and time : {}/{} {}:{}".format(x.month,x.day,x.hour,x.second))
grocery = ["Parmesan","Mozarella"]
print("You currently have Parmesan and Mozeralla in your list.\n")


for i in range(3) :
    food = input("Type of food to add to the grocery list : ")
    grocery.append(food.title())


print("\nHere is your grocery list : ")
print(grocery)
print("Here is your grocery list sorted : ")
grocery.sort()
print(grocery)

print("\nSimulating grocery shopping...\n")

food = 0
while len(grocery) != 2 :
    print("Current grocery list : {} items".format(len(grocery)))
    print(grocery)
    food = input("What food did you just buy : ").title()
    grocery.remove(food)
    print("Removing {} from your list...\n".format(food))


print("Sorry the store is out of {}".format(grocery[1]))
food = input("What food would you like instead : ")
grocery.pop()
grocery.append(food)

print("\nHere is what remains on your grocery list")
print(grocery)