import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    
    # Check the format
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        
        # Split the number
        number_list = ip.split('.')
        
        for num in number_list:
            if int(num) < 0 or int(num) > 255:
                return False
        
        return True

    else:
        return False                


if __name__ == "__main__":
    main()