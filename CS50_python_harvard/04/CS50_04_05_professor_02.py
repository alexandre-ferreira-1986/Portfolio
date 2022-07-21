import random


def main():
    level = get_level()

    score = game(level)
    
    print('Score: ', score)

def get_level():
    
    while True:
        try:
            level = int(input('Level: '))
            if level >= 1 and level <=3:
                return level
                
        except:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    
    if level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    
    if level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)

    
    return x, y


def error(x, y):
    errors = 1
    while errors <= 3:
        try:
            answer = int(input(f'{x} + {y} = '))
            if answer == (x + y):
                return True
            else:
                errors += 1
                print('EEE')
        
        except:
            errors += 1
            print('EEE')
    print(f'{x} + {y} = {x+y}')
    return False

def game(level):
    math_problem = 1
    score = 0
    while math_problem <= 10:
        x, y = generate_integer(level)
        resp = error(x, y)
        if resp == True:
            score += 1
        
        math_problem += 1
    
    return score
        
        
        
        
        

if __name__ == "__main__":
    main()