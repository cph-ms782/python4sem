
import random
from os.path import isfile, join
import os
import csv


class Student():
    """A student Class"""

    def __init__(self,  name, gender, data_sheet, image_url):
        """Initialize Student with name, gender, data_sheet and image_url"""
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def __repr__(self):
        return 'Student(%r, %r, %r, %r)' % (self.name, self.gender,
                                            self.data_sheet, self.image_url)

    def __str__(self):
        return '{name} is {gender} has {data_sheet} and looks like {image_url}.'.format(
            name=self.name, gender=self.gender, data_sheet=self.data_sheet, image_url=self.image_url)

    def get_avg_grade(self):
        """Student - get_avg_grade"""
        pass


class DataSheet():
    """ DataSheet """

    def __init__(self, courses):
        """Initialize Datasheet with courses"""
        self.courses = courses

    def __repr__(self):
        return 'DataSheet(%r)' % (self.courses)

    def __str__(self):
        return 'DataSheet: courses are {courses}'.format(
            courses=self.courses)

    def get_grades_as_list(self):
        """DataSheet - get_grades_as_list"""
        pass


class Course():
    """Course"""

    def __init__(self, name, classroom, teacher, ETCS, optional_grade=0):
        """Initialize Course with name, classroom, teacher, ETCS and optional grade if course is taken"""
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.optional_grade = optional_grade

    def __repr__(self):
        return 'Course(%r, %r, %r, %r, %r)' % (self.name, self.classroom,
                                               self.teacher, self.ETCS, self.optional_grade)

    def __str__(self):
        return '{name} is in {classroom} has {teacher} which gives {ETCS} and can give optionally {optional_grade}.'.format(
            name=self.name, classroom=self.classroom, teacher=self.teacher, ETCS=self.ETCS, optional_grade=self.optional_grade)


def generate_students(n):
    """ Generate n number of students """

    names = ["Borneo", "Gentri", "Jethro"]
    teachers = ["Hans Jørgensen", "Jens Hansen", "Hans Jensen"]
    courses_list = ["Dansk", "Engelsk", "Matematik"]
    class_rooms = range(1, 20)
    urlLibs = ["1.jpg", "2.jpg", "3.jpg"]
    gender = ["male", "female"]
    grades = [4, 7, 10, 12]

    students = []
    courses = []
    for i in range(n):
        courses.append(Course(random.choice(courses_list), random.choice(
            class_rooms), random.choice(teachers), 10, random.choice(grades)))
        data_sheet = DataSheet(courses)
        student = Student(random.choice(names)+"#"+str(i), random.choice(
            gender), data_sheet, random.choice(urlLibs))
        students.append(student)
    return students


def write_list_to_file(output_file, list):
    """can take a list of tuple and write each element to a new line in file"""
    if output_file != None:
        with open(output_file, "w") as output:
            student_writer = csv.writer(
                output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            student_writer.writerow(["stud_name", "course_name", "teacher", "ects", "classroom", "grade", "img_url"])
            for el in list:
                print("el", el)
                for c in el.data_sheet.courses:
                    student_writer.writerow([el.name, c.name, c.teacher, c.ETCS, c.classroom, c.optional_grade, el.image_url])
    else:
        for line in list:
            print(line)


studs = generate_students(22)
print(studs)
write_list_to_file("students.csv", studs)
