#with Manual Comments
# Define a class to represent a SRU student
class sru_student:
    # Constructor to initialize the student object
    def __init__(self, name, roll_no, hostel_status):
        # Store the name of the student
        self.name = name
        # Store the roll number of the student
        self.roll_no = roll_no
        # Store the hostel status (True/False)
        self.hostel_status = hostel_status

    # Method to update the student's fee status
    def fee_update(self, status):
        # Update the hostel_status attribute with the new value
        self.hostel_status = status
        # Print confirmation message
        print(f"Fee status updated to {self.hostel_status} for {self.name}")

    # Method to display all student details
    def display_details(self):
        # Print the student's name
        print(f"Name: {self.name}")
        # Print the student's roll number
        print(f"Roll Number: {self.roll_no}")
        # Print the hostel status
        print(f"Hostel Status: {self.hostel_status}")


# Create a student object
student1 = sru_student("Alice", "SRU101", True)

# Display the student's details
student1.display_details()

# Update the student's hostel fee status
student1.fee_update(False)

# Display updated details
student1.display_details()
 