print("Welcome to the average calculator app")
name = input("What is your name : ")
num = int(input("How many grades would you like to enter : "))
grades = []
for _ in range(num) :
    grades.append(int(input("Enter grade : ")))

grades.sort()
grades.reverse()
print("\nGrades highest to lowest : ")
for i in range(num)  :
    print(grades[i])

print("\n{}'s Grades summary :".format(name))
print("Total number of grades : {}".format(num))
print("highest grade : {}".format(grades[0]))
print("lowest grade : {}".format(grades[-1]))
print("Average : {}".format(sum(grades)/num))

des = float(input("What is your desired average : "))

print("Good luck {}".format(name))
print("You will need to get a {} on your next test.".format((des-sum(grades)/(num+1))*(num+1)))