print("Welcome to the Grade Sorter App")

grades = []
grade1 = float(input("\nWhat is your first grade (0-100): "))
grades.append(grade1)
grade2 = float(input("What is your second grade (0-100): "))
grades.append(grade2)
grade3 = float(input("What is your third grade (0-100): "))
grades.append(grade3)
grade4 = float(input("What is your forth grade (0-100): "))
grades.append(grade4)
grades.sort(reverse=True)
print("\nYour grades are :",grades)
print("\nThe lowest two grades will now be dropped.")
print("Removed grade :",grades.pop())
print("Removed grade :",grades.pop())

print("\nYour remaining grades are :",grades)
print("Nice work! Your highest grade is a",grades[0])

