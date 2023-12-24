from datetime import datetime


class Person:
    def __init__(self, name, country, birth):
        self.name = name
        self.country = country
        self.birth = birth
    def calculate_age(self):
        today = datetime.today()   
        age = today.year - self.birth.year
        return age

person = Person("james", "france", datetime(2000, 7, 12))
print(person.calculate_age)
