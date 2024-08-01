# The length of the input sentence
str_manip = input("Please enter a sentence: ")
print(len(str_manip))

# The last letter of the input sentence 
# Every occurrence of the last letter replaced by '@'
last_letter = str_manip[-1]
print(last_letter)
print(str_manip.replace(last_letter, "@"))

# The last three characters of the inputted sentence reversed
print(str_manip[-3:][::-1])

# A five letter word created from the first three characters of the input sentence and the last two characters
print(str_manip[:3] + str_manip[-2:])