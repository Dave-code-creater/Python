"""
Module Name: class.py
Description: This module contains the class Student
which is used to perfome the following operations:
- Ranking students based on their GPA
- Ranking students based on their physic score
- Ranking students based on their math score
- Ranking students based on their science score
- Order students based on their name
- Order students based on their date of birth
"""

from student import Student

class Lab(): 
    """
    Represent a school class
    """
    def __init__(self, name: str):
        self.name = name
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    # TODO: Implement the methods that rank students based on their GPA.
    # physic score, math score, science score, name, and date of birth
    def rank_by_gpa(self) -> list:
        pass

    # TODO: Implement the methods that order studnet based on thier GPA.
    def order_by_gpa(self) -> list:
        pass

    # TODO: Implement the methods that rank students based on their physic score.
    def rank_by_physic(self) -> list:
        pass

    # TODO: Implement the methods that order studnet based on thier math score. 
    def order_by_math(self) -> list:
        pass

    def order_by_name(self) -> list:
        return sorted(self.students, key=lambda x: x.name)
    
    def order_by_dob(self) -> list:
        return sorted(self.students, key=lambda x: x.dob)
    
    def __str__(self) -> str:
        return f"Class {self.name} has {len(self.students)} students"