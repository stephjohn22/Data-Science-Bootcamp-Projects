# Asks user to input their time for each part of the triathlon
swim = int(input("How many minutes did you spend swimming? "))
cycle = int(input("How many minutes did you spend cycling? "))
run = int(input("How many minutes did you spend running? "))

# Calculates the total time completing the triathlon
triathlon_time = swim + cycle + run
print(triathlon_time)

# Prints a string notifying the user if they were within qualifting time and what award they have achieved 
if triathlon_time <= 100:
    print("Congratulations, you were within the qualifying time and have been awarded Provinvial colours!")

elif  101 >= triathlon_time <= 105:
    print("Congratulations, you were within five minutes of the qualifying time and have been awarded Provincial half colours!")

elif 106 >= triathlon_time <= 110:
    print("Congratulatons, you were within ten minutes of the qualifying time and have been awarded Provincial scoll")

elif triathlon_time >= 111:
    print("Unfortunately you were more than ten minutes off from the qualifying time and have not received an award this time.")