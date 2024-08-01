# User enters three integer seperated by spaces
num1, num2, num3 = input("Enter three different integers: ").split()

# The sum of the integers
print(int(num1) + int(num2) + int(num3))

# The first number minus the second number
print(int(num1) - int(num2))

# The third integer multiplied by the first number
print(int(num3) * int(num1))

# The sum of all three numbers divided by the third number
print((int(num1) + int(num2) + int(num3)) / int(num3))