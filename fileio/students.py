import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})





























# import csv
# # with open("students.csv") as file:
# #     for line in file:
# #         name, house = line.rstrip().split(",")
# #         print(f"{name} is in {house}")


# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# # def get_name(student):
# #     return student["name"]

# # def get_house(student):
# #     return student["house"]

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")