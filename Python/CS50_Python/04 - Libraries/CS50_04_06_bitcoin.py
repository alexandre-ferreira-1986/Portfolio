# import sys to get the arguments
import sys

# import 'requests' to get the data of an website
import requests


# The user has to pass the value of bitcoins
if len(sys.argv) == 2:
    
    # Check if the value is an float
    try:
        coin = float(sys.argv[1])
    
    
    # If the user input a value that is not a number:
    except:
        print('Command-line argument is not a number ')
        sys.exit(1)

# If the user doesn't pass a number of bitcoins, print an error
else:
    print('Missing command-line argument')
    sys.exit(1)
    

# Get the value of the bitcoin
try:
    # use the website passed by CS50
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    
    # convert the informations to JSON
    resp = r.json()
    
    # getting the 'USD float' value of bitcoin
    bitcoin = resp['bpi']['USD']['rate_float']
    
    my_amount = bitcoin * coin
    print(f'${my_amount:,.4f}')
    
except requests.RequestException:
    print('RequestException')
    sys.exit(1)