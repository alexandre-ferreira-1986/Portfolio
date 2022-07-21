
def main():
    text = input('Input: ')
    
    vogals = ['a', 'e', 'i', 'o', 'u']
    new_str = ''
    
    for i in text:
        if i.lower() in vogals:
            continue
        else:
            new_str += i
            
    print('Output: ', new_str)
    
    
    
if __name__ == "__main__":
    main()