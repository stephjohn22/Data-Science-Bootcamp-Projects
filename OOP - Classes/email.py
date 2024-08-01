class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

# Initialise an empty variable
inbox = []

# Function to populate the inbox with sample emails
def populate_inbox():
    inbox.append(Email("person1@email.com", "Welcome to HyperionDev", "Welcome to the bootcamp!"))
    inbox.append(Email("person2@email.com", "Great work on the bootcamp!", "You are progessing well!"))
    inbox.append(Email("person3@email.com", "Your excellent marks!", "Well done on your recent submission!"))

# Function to list all emails with their indices
def list_emails():
    for index, email in enumerate(inbox):
        print(f"\n{index} {'(Read)' if email.has_been_read else '(Unread)'} - {email.subject_line}")

# Function to read a specific email by index
def read_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        email.mark_as_read()
        print(f"\nFrom: {email.email_address}\nSubject: {email.subject_line}\nContent: {email.email_content}\n")
    else:
        print("\nInvalid option. Please try again.")

# Populate inbox with sample emails at startup
populate_inbox()

# Main program loop
while True:
    print("""\nWould you like to:
1. Read an email
2. View unread emails
3. Quit application""")
    user_choice = input("\nEnter your chosen option: ")

    if user_choice == "1":
        list_emails()
        email_index = int(input("\nEnter the number of the email you wish to read: "))
        read_email(email_index)
    elif user_choice == "2":
        unread_exists = False
        for email in inbox:
            if not email.has_been_read:
                print(f"\n(Unread) {email.subject_line}")
                unread_exists = True
        if not unread_exists:
            print("You have no unread emails.")
    elif user_choice == "3":
        break
    else:
        print("\nPlease input one of the valid options (1 , 2 or 3).")