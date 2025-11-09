class Student:
    """
    A simple Student class that stores student details
    and provides a method to display student information.
    """

    def __init__(self, name, age, student_id, grade):
        # Attributes
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grade = grade

    def display_info(self):
        """Method to display the student's information."""
        print("---- Student Information ----")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Grade: {self.grade}")
        print("-----------------------------")


# Example usage (you can modify these values)
student1 = Student("Alice Johnson", 20, "S12345", "A")
student2 = Student("Bob Smith", 19, "S67890", "B+")

# Calling the method to check the output
student1.display_info()
student2.display_info()
