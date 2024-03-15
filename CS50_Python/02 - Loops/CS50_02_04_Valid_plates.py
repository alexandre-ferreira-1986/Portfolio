def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Chacking the first 2 items
    # isalpha():  https://docs.python.org/3/library/stdtypes.html
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    
    # The first number can't be 0 (zero)
    for i in range(len(s)):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
    
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
    
    for char in s:
        if char in ['.', ' ', '?', '!']:
            return False
        
    return True


if __name__ == '__main__':
    main()