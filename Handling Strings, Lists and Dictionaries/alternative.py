# Variable Random  
name = "this is a skills bootcamp task"

name1 = ""
# Makes the string alternate each character between uppercase and lowercase
for a in range(len(name)):
    if a % 2 == 0:
        name1 += name[a].lower()
    else:
        name1 += name[a].upper()

print(name1)

# Splits each word in the string
name = name.split()
# Makes each word in the string alternate between uppercase and lowercase
for a in range(len(name)):
    if a % 2 == 0:
        name[a] = name[a].lower()
    else:
        name[a] = name[a].upper()

# Prints the variable rejoined 
print(" ".join(name))