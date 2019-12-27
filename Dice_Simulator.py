import random                             #imports random module

def roll_dice():
    inp = input("Do you want 1 die or 2 dice ? :")

    if(inp == 1):
        r1 = random.randint(1,6)
        print "Rolling the dices....."
        print "The values are........"
        print("The top face of the die shows %s" % r1)


    else:
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        add = r1 + r2
        print "Rolling the dices....."
        print "The values are........"
        print ("The top face of the first die shows %s" %r1)
        print ("The top face of the second die shows %s" %r2)

if __name__ == '__main__':
    start = raw_input("Do you want to roll dices? : ")
    if(start == 'yes' or start == 'YES'):
        roll_dice()
        roll_again = raw_input("Do you want to roll the dices again ? : ")
        while roll_again == 'YES' or roll_again == 'yes' or roll_again == 'y' or roll_again == 'Y':
            roll_dice()
            roll_again = raw_input("Do you want to roll the dices again ? : ")
