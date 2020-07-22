print("Welcome to the Yes or No issue polling app\n")

message = input("What is the yes/no issue you will be voting on today : ")
voters = int(input("What is the number of voters you will allow on this issue : "))
passw = input("Enter a password for polling voters : ")


response = {}


for i in range(voters) :
    name = input("Enter your full name : ")
    print("today's issue is : {}".format(message))
    boole = input("What do you think .... yes or no : ")
    if name not in response :
        response[name] = boole
    else :
        print("Sorry it seems you have already voted.")
    print("Thank you {}! your vote of {} has been recorded.".format(name,boole))


print("\nThe following {} people voted".format(len(response.keys())))
for i in response.keys() :
    print(i)


print("\nOn the following issue : {}".format(message))
count_yes = 0
count_no = 0

for i in response.values() :
    if i == 'yes' :
        count_yes += 1
    elif i == 'no' :
        count_no += 1


if(count_no > count_yes) :
    print("No wins! {} votes to {}".format(count_no,count_yes))
elif count_yes > count_no :
    print("Yes wins! {} votes to {}".format(count_yes,count_no))
else :
    print("it was a tie! {} votes to {}".format(count_no,count_yes))

con_passw = input("To see the voting results enter admin password : ")
if con_passw == passw :
    for key,val in response.items() :
        print("{} ----> {}".format(key,val))