"""
Module Name: student.py
Description: This module contains the class Student 
which is used to store the information of a student.
Author: Ta, Tan Dat
Date: Feb 11, 2025
"""

class Student:
    """
    A student has the following attributes:
    - id: student ID
    - name: student name
    - dob: student date of birth
    - gpa: student GPA
    - physic: student physical score
    - math: student math score
    - science: student science score
    """

    def __init__(self) -> None:
        self.id = None
        self.name = None
        self.dob = None
        self.gpa = None
        self.physic = None
        self.math = None
        self.science = None

        def get_id(self):
            return self.id

        def set_id(self, id):
            self.id = id

        def get_name(self):
            return self.name

        def set_name(self, name):
            self.name = name

        def get_dob(self):
            return self.dob

        def set_dob(self, dob):
            self.dob = dob

        def get_gpa(self):
            return self.gpa

        def set_gpa(self, gpa):
            self.gpa = gpa

        def get_physic(self):
            return self.physic

        def set_physic(self, physic):
            self.physic = physic

        def get_math(self):
            return self.math

        def set_math(self, math):
            self.math = math

        def get_science(self):
            return self.science

        def set_science(self, science):
            self.science = science

    def __str__(self) -> None:
        print(f"Here is the information of the student with ID {self.id}:")
        print(f"Name: {self.name}")
        print(f"Date of birth: {self.dob}")
        print(f"GPA: {self.gpa}")
        print(f"Physic score: {self.physic}")
        print(f"Math score: {self.math}")
        print(f"Science score: {self.science}")
        return 

    # TODO: write a method to calculate the average score of the student
    def get_average_score(self) -> float:
        pass

    # TODO: write into a pdf file the report of each of the student
    def generate_report(self) -> None:
        pass
    