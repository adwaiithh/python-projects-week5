from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def course_details(self):
        pass


class ProgrammingCourse(Course):
    def __init__(self, course_name, duration, language):
        super().__init__(course_name, duration)
        self.language = language

    def course_details(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Programming Language:", self.language)
        print("-----------------------------")


class DesignCourse(Course):
    def __init__(self, course_name, duration, software):
        super().__init__(course_name, duration)
        self.software = software

    def course_details(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Design Software:", self.software)
        print("-----------------------------")


class MarketingCourse(Course):
    def __init__(self, course_name, duration, specialization):
        super().__init__(course_name, duration)
        self.specialization = specialization

    def course_details(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Marketing Specialization:", self.specialization)
        print("-----------------------------")


prog = ProgrammingCourse("Python Development", "3 Months", "Python")
design = DesignCourse("Graphic Design", "2 Months", "Photoshop")
marketing = MarketingCourse("Digital Marketing", "4 Months", "SEO")

courses = [prog, design, marketing]

for course in courses:
    course.course_details()