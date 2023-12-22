class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.__courses = {}

    def calculate_letter_grade(self, score):
        self.score = score
        if self.score >= 90:
            return "A"
        elif self.scofre >= 80 or self.score <= 89:
            return "B"
        elif self.score >= 70 or self.score <= 79:
            return "C"
        elif self.score >= 60 or self.score <= 69:
            return "D"
        else:
            return "F"

    def add_course(self, course_name, score):
        pass

    def get_courses(self):
        return self.__courses
