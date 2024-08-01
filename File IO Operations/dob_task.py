names = []
birthdates = []
# Seperate the full names in the txt file from the birthdates
with open("DOB.txt", "r") as file:
    for line in file:
        separate = line.strip().split()
        name = ' '.join(separate[:2])
        birthdate = ' '.join(separate[2:])

        names.append(name)
        birthdates.append(birthdate)

# Print all the full names on individual lines
print("Name")
for name in names:
    print(name)

# Print all the birthdates on individual lines
print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)