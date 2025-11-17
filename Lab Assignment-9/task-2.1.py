#AI-Generated Inline Comments

class sru_student:
    def __init__(self, name, roll_no, hostel_status):
        self.name = name  # Assign input name to instance variable
        self.roll_no = roll_no  # Assign input roll number to instance variable
        self.hostel_status = hostel_status  # Assign input hostel status to instance variable

    def fee_update(self, status):
        self.hostel_status = status  # Update the hostel status with the given status
        print(f"Fee status updated to {self.hostel_status} for {self.name}")  # Print confirmation of update

    def display_details(self):
        print(f"Name: {self.name}")  # Display the student's name
        print(f"Roll Number: {self.roll_no}")  # Display the student's roll number
        print(f"Hostel Status: {self.hostel_status}")  # Display the hostel status

student1 = sru_student("Alice", "SRU101", True)  # Create a new student object with name, roll number, and hostel status
student1.display_details()  # Call method to display student details
student1.fee_update(False)  # Update hostel fee status to False
student1.display_details()  # Display updated details
