import inflect
p = inflect.engine()
#prompts user for names 
#store user data
#format gramatically
#if two names separate with and
#if three names separate with two commas and and
names = []
song = "Adieu, adieu, to "
while True:
    try:
        name = input("Name: ")
        names.append(name)
        pass
    except EOFError:
        break
        print("\n")
    
print("\n")
print(song, end = "")
print(p.join(names))
