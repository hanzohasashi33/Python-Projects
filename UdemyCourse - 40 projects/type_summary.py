def summary(l) :
	print("The variable is of",type(l))
	print("It contains the elements",l)
	print("The element ",str(l[0])," is a ",type(l[0]))
	print("\n")

num_strings = ['15','100','55','42']
num_ints = [15,100,55,42]
num_floats = [2.2,5.0,1.245,0.14287]
num_lists = [[1,2,3],[4,5,6],[7,8,9]]


print("Summary Table".center(100))
print("\n")
summary(num_strings)
summary(num_ints)
summary(num_floats)
summary(num_lists)


num_ints.sort()
num_strings.sort()
print("\nNow sorting the num_strings and num_ints")
print("Sorted num_strings : ",num_strings)
print("Sorted int_strings : ",num_ints)
print("\n Strings are sorted alphabetically and integers are sorted numerically!")