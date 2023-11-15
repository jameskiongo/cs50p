import random
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass
    
n = random.randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            pass
        else:
            if guess < n:
                print("Too small!")
                pass
            elif guess > n:
                print("Too large!")
                pass
            else:
                print("Just right!")
                break
    except:
        None