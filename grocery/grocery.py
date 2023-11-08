# prompt user for items, one per line
grocery = {}

while True:
    try:
        item = input().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except KeyError:
        pass
    except EOFError:
        for key in sorted(grocery.keys()):
            print(grocery[key], key)
        break

# control d to exit program
# output list in all uppercase, sorted alphabetically by item
# number of times user inputted that item
