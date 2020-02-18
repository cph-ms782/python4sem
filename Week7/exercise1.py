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
    import random

    names = ["Borneo", "Gentri", "Jethro"]
    courses = ["Dansk", "Engelsk", "Matematik"]
    class_rooms = range(1, 20)
    urlLibs = ["1.jpg", "2.jpg", "3.jpg"]
    gender = ["male", "female"]
    grades = [4, 7, 10, 12]

    students = []
    for i in range(n):
        course = Course(random.choice(courses), random.choice(
            class_rooms), random.choice(names), random.choice(grades))
        data_sheet = DataSheet([course])
        student = Student(random.choice(names)+"#"+str(i), random.choice(
            gender), data_sheet, random.choice(urlLibs))
        students.append(student)
    return students


print(generate_students(2))
