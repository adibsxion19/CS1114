#Aadiba Haque
#Lab 13 Problem 4
#May 1 2020
class Student:
    def __init__(self, name, NYU_id, net_id):
        self.name = name
        self.NYU_id = NYU_id
        self.net_id = net_id
        self.grades_list = []
    def add_grade(self, catalog_name, grade):
        self.grades_list.extend([catalog_name,grade])
    def average(self):
        summation = 0
        count = 0
        for i in grades_list:
            count +=1
            summation += i[1]
        return round(summation/count,0)
    def get_email(self):
        return "{}@nyu.edu".format(self.net_id)
    def load_students(filename):
        file.readlines()
        for lines in file:
            lines = lines.strip()
            student = Student()
        file.close()
        return student.split()
    def generate_performance_report(students_lst):
        return self.NYU_id, self.average()
    def generate_course_mailing_list(students_lst, catalog_name):
        student_data = self.add_grade
        if students_lst in student_data and catalog_name in student_data:
            return get_email()
    def main():
        file = open("grades.csv","r")
        print(Student.generate_performance_report(load_students(file)))
        print(Student.generate_course_mailing_list(load_students(file)))
    main()
    