import sys
while True:
    try:
        n = int(input("No: "))
        break
    except ValueError:
        pass
    # else:
    #     break
print(n)
