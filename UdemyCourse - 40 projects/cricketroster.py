print("Welcome to the cricket Roster Program\n")
l = []
for i in range(5) :
    if i == 0 :
        player = input("Who is your captain : ")
        l.append(player)
    elif i == 1 :
        player = input("Who is your bowler : ")
        l.append(player)
    elif i == 2 :
        player = input("Who is your batsman : ")
        l.append(player)
    elif i == 3 :
        player = input("Who is your all-rounder : ")
        l.append(player)
    else :
        player = input("Who is your keeper : ")
        l.append(player)

l = [x.title() for x in l]

print("\n\tYour starting 5 for the upcoming cricket match")
print("\t\tcaptain :\t\t{}".format(l[0]))
print("\t\tbowler :\t\t{}".format(l[1]))
print("\t\tbatsmen :\t\t{}".format(l[2]))
print("\t\tall-rounder :\t\t{}".format(l[3]))
print("\t\tkeeper :\t\t{}".format(l[4]))

injured = l.pop()
print("\nOh no, {} is injured.".format(injured))
print("You currently have only {} players in your roster".format(len(l)))
player = input("Who do you want to replace {} with :".format(injured))
l.append(player.title())

print("\n\tYour starting 5 for the upcoming cricket match")
print("\t\tcaptain :\t\t{}".format(l[0]))
print("\t\tbowler :\t\t{}".format(l[1]))
print("\t\tbatsmen :\t\t{}".format(l[2]))
print("\t\tall-rounder :\t\t{}".format(l[3]))
print("\t\tkeeper :\t\t{}".format(l[4]))

print("\nGood luck {} will do you great!".format(player))