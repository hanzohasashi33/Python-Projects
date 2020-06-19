from math import sqrt

print("Welcome to the Right Triangle Solver App\n")

a = float(input('What is the first leg of the triangle : '))
b = float(input('What is the second leg of the triangle : '))
c = sqrt(a**2 + b**2)

area = 0.5 * b * a
print("hypotenuse is {}".format(round(c,4)))
print("area is {}".format(round(area,2)))
