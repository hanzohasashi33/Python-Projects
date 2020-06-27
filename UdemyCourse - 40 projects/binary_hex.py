print("Welcome to the Binary/Hexadecimal Converter App\n")

num = int(input("Compute binary and hexadecimal values upto the following decimal number : "))

binary = []
hexadecimal = []

for i in range(0,num+1) :
    binary.append(bin(i))
    hexadecimal.append(hex(i))

print("Generating lists....complete")
print("\nUsing slices,we will now show a portion of each list")
start = int(input("Start at : "))
end = int(input("end at : "))

print("\nDecimal values from {} to {}".format(start,end))
for i in range(start,end + 1) :
    print(i)

print("\nBinary values from {} to {}".format(start,end))
for i in range(start,end + 1) :
    print(binary[i])

print("\nHexadecimal values from {} to {}".format(start,end))
for i in range(start,end + 1) :
    print(hexadecimal[i])

print("\nAll nums")
for i in range(num + 1) :
    print("{}----{}----{}".format(i,binary[i],hexadecimal[i]))