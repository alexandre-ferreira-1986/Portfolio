import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    
    while True:
        try:
            level = int(input('Level: '))
            if level >= 1 and level <=3:
                return level
                
        except:
            pass


def generate_integer(level):
    try:
        math_problem = 1
        score = 0
        error = 0 
        if level == 1:
            while math_problem <= 10:
                x = random.randint(0,9)
                y = random.randint(0,9)
                soma = x + y
                ans = int(input(f'{x} + {y} = '))
                if ans == soma:
                    score += 1
                else:
                    while error < 4:
                        error += 1
                        print('EEE')
                        ans = int(input(f'{x} + {y} = '))
                        if ans == soma:
                            score += 1
                            break    
                        if error == 3:
                            print(f'{x} + {y} = {x + y}')
                            error = 0
                            break
                        
                
                math_problem += 1
            print('Score: ', score)
    except: 
        pass



if __name__ == "__main__":
    main()