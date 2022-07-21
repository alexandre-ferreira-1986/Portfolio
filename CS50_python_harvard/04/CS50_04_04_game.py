import random



while True:
    try: 
        lev = int(input('Level: '))
        
        if lev >= 1:
            rand_num = random.randint(1, lev)
            break
    except:
        
        pass


while True:
    try:
        num_choice = int(input('Guess: '))
        if num_choice > rand_num:
            print('Too large!!')
        elif num_choice < rand_num:
            print('Too small!!')
        else:
            print('Just right!')
            break
        
        
    
    except:
        pass
        
    

