print("Welcome to the frequency analysis app")

message = input("Enter a word or phrase to count : ")
print("\nHere is the frequency analysis of the string.\n")

freq = {}

message = message.replace(" ","").replace(".","")
message = message.lower()
for i in message : 
    if i.isalpha() :
        if i in freq :
            freq[i] += 1
        else :
            freq[i] = 1


total = 0
for i in freq.values() :
    total += i 


print("Letter\t\tOccurance\t\tPercentage")
for key,val in freq.items() :
    print("{}\t\t{}\t\t\t{}%".format(key,val,val*100/total))


print("\nLetters sorted for max occurance to least occurance : ")
sorted_dict = dict(sorted(freq.items(),key=lambda kv: (kv[1],kv[0]),reverse=True))
for i in sorted_dict.keys() :
    print(i,end="")
print()