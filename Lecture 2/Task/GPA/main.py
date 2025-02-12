from lab import Lab
from student import Student
import csv

def read_students_from_csv(file_path: str) -> list:
    students = []
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            student = Student()
            student.set_id(row['id'])
            student.set_name(row['name'])
            student.set_dob(row['dob'])
            student.set_gpa(row['gpa'])
            student.set_physic(row['physic'])
            student.set_math(row['math'])
            student.set_science(row['science'])
            students.append(student)
    return students


def main():
    students = read_students_from_csv('students.csv')
    lab = Lab('Winter 2021')
    for student in students:
        lab.add_student(student)
    print(lab)
    print(f"The highest GPA student is:", lab.rank_by_gpa()[0])
    print(f"The lowest GPA student is:", lab.rank_by_gpa()[-1])
    print(f"The highest physic score student is:", lab.rank_by_physic()[0])
    print(f"Class order by name:", lab.order_by_name())

if __name__ == "__main__":
    main()