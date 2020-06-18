print("Welcome to the Temperature Conversion Program\n")

faren = float(input('What is the given temperature in degrees Farenheit : '))
celsius = round(((faren - 32) * (5/9)),4)
kelvin = round((celsius + 273.15),4)
print("\n")
print("Degrees Fahreneheit :\t {}".format(faren))
print("Degrees Celsius :\t {}".format(celsius))
print("Degrees Kelvin :\t {}".format(kelvin))
