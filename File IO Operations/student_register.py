# Ask user to input the number of students registering
def exam_students():
    number_of_students = int(input("How many students are registering? "))
    
    # Create a txt file that holds the inforamtion about the students taking the exam and overwrites if the file already exists
    with open("reg_form.txt", "w+") as file:
        # Ask the user for the student ID number for each student registering
        for num in range(number_of_students):
            student_id = input(f"What is the student ID number for student {num+1}: ")
            file.write(f"{student_id}  ...................\n\n")

# Sends the registering students' information to the txt file
if __name__ == "__main__":
    exam_students()