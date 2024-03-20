import random


def main():
    level = get_level()
    score = generate_integer(level)
    print(score)


def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if level >=1 and level <= 3:
                return level
        except:
            pass

def generate_integer(level):
    score = 0

    for i in range(10):
        attempts = 0
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        # Check the answer
        while attempts <= 2:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    attempts += 1
                    print("EEE")
            except:
                errors += 1
                print("EEE")
                
        if attempts > 2:
            print(f'{x} + {y} = {x+y}')

    return score

if __name__ == "__main__":
    main()