import math 


print("Welcome to the Quadratic Solver App")

a = float(input('a :'))
b = float(input('b :'))
c = float(input('c :'))

D = b**2 - 4*a*c   

if D > 0 :
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print("Roots are {} and {}".format(x1,x2))

elif D < 0 :
    x1 = (-b)/(2*a)
    x2 = (-b)/(2*a)
    imag = math.sqrt(-D)/(2*a)
    print("Roots are {} + {}i and {} - {}i".format(x1,imag,x2,imag))

else :
    x1 = (-b)/(2*a)
    x2 = (-b)/(2*a)
    print("Roots are {} and {}".format(x1,x2))
