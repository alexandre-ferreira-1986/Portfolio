from validator_collection import validators


def main():
    
    email_input = input("What's your email address? ")
    
    try:
        is_email_valid = validators.email(email_input)
        print('Valid')
    
    except:
        print('Invalid')
    
    
    
if __name__ == '__main__':
    main()