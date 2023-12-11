# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#     for line in file:
#         print(f"hello, {line.rstrip()}")

names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names, reverse=True):
    print(f"hello, {name}")