print("Welcome to the shipping accounts program")

name = input("What is your name : ")
print("hello {},welcome to your account")
print("current shipping prices are us follows : \n")
print("shipping order 0 to 100\t\t\t$5.10 each")
print("shipping order 100 to 500\t\t$5.00 each")
print("shipping order 500 to 1000\t\t$4.95 each")
print("shipping orders over 1000\t\t$4.80 each")

quantity = int(input("How many items would you like to ship : "))
if quantity < 100 :
    print("To ship {} items it will cost you {} at ${} per item".format(quantity,round(quantity*5.10,2),5.10))
elif quantity < 500 :
    print("To ship {} items it will cost you {} at ${} per item".format(quantity,round(quantity*5.00,2),5.00))
elif quantity < 1000 :
    print("To ship {} items it will cost you {} at ${} per item".format(quantity,round(quantity*4.95,2),4.95))
else :
    print("To ship {} items it will cost you {} at ${} per item".format(quantity,round(quantity*4.80,2),4.80))

dec = input("Would you like to place the order(y/n) : ")
if dec == 'y' : 
    print("Your order is placed")
else :
    print("okay, no order is being placed this time.")