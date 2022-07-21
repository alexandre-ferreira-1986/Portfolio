import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    
    # Check if the input is correct (Frame... /frame)
    if re.search(r'<iframe(.)*><\/iframe>', s):
        
        # Now look for the youtube pattern
        url_pattern =  re.search(r'(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)', s)
        
        # If it is correct, split the information
        if url_pattern:
            
            split_url = url_pattern.groups()
            
            return "https://youtu.be/" + split_url[3]



if __name__ == "__main__":
    main()