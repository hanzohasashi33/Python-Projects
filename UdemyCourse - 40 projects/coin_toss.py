from random import choice

print("Welcome to the coin toss app.")

print("\nI will flip a coin a set number of times")
times = int(input("How many times would you like me to flip the coin : "))
prin = input("Would you like to see the result every time(y/n) : ")
coin = ["HEADS","TAILS"]
head_count = 0
tail_count = 0
for _ in range(times) :
    result = choice(coin)
    if prin == 'y' : 
        print(result)
    
    if result == "HEADS" :
        head_count += 1 
    else :
        tail_count += 1

print("\nResults of flipping a coin {} times:\n".format(times))
print("Side\t\tCount\t\tPercentage")
print("Heads\t\t{}\t{}".format(str(head_count)+"/"+str(times),head_count*100/times))
print("Tails\t\t{}\t{}".format(str(tail_count)+"/"+str(times),tail_count*100/times))
