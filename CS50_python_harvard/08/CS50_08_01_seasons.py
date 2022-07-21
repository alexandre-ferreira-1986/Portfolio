import re
import sys
from datetime import date
import inflect

p = inflect.engine()


def main():
    
    # Input the date of the birth
    birth_date = input('Date of Birth: ')
    
    try:
        year, month, day = check_birthday(birth_date)
        
    except:
        sys.exit('Invalid Date')
    
    date_of_birth = date(int(year), int(month), int(day))
    
    today_date = date.today()
    
    diff_date = today_date - date_of_birth
    
    total_minutes = diff_date.days * 24 * 60
    
    output = p.number_to_words(total_minutes, andword = '')
    
    print(output.capitalize() + ' minutes')
    

def check_birthday(birth_date):
    
    if re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', birth_date):
        year, month, day = birth_date.split('-')
        return year, month, day


if __name__ == "__main__":
    main()