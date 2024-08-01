middle_stars = 5
# Prints out a pattern of stars where the middle line has 5 stars and it decreases on each line above and below the middle line
for i in range(1, 2 * middle_stars):
    if i <= middle_stars:
        print("*" * i)
    else:
        print("*" * (2 * middle_stars - i))