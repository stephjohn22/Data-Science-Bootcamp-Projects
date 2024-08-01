num_sum = 0
count = 0

# Asks user to continuously enter a number and input -1 to stop entering numbers
while True:
    num = input("Enter a number or type -1 to stop: ")

    # calculates the sum of the inputted numbers when the user indicates to stop
    if num == "-1":
        break
    num = int(num)
    num_sum += num
    count += 1

# Calculates the average of the inputted numbers
if count > 0:
    average = num_sum / count
    print("The average of the numbers is: ",  average)

else:
    print("Please enter a number before you stop")