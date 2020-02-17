class Student():
    """A student Class"""

    def __init__(self,  name, gender, data_sheet, image_url):
        """Initialize Student with name, gender, data_sheet and image_url"""
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def __repr__(self):
        return 'Student(%r, %r, %r)' % (self.name, self.gender,
                                        self.data_sheet, self.image_url)

    def __str__(self):
        return '{name} is {gender} has {data_sheet} and looks like {image_url}.'.format(
            name=self.name, gender=self.gender, data_sheet=self.data_sheet, image_url=self.image_url)

    def get_avg_grade(self):
        """Student - get_avg_grade"""
        pass


class DataSheet():

    def __init__(self, courses):
        """Initialize Datasheet with courses"""
        self.courses = courses

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


def generate_students(self):
    pass
