from twttr import shorten

def main():
    
    # Test the upper and lower cases    
    test_up_low_cases()
    
    # Test ponctuation, space and number
    test_ponctuation()
    
    

def test_up_low_cases():
    
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwItTeR') == 'TwtTR'

def test_ponctuation():
    assert shorten("What's 12?") == "Wht's 12?"  
    
if __name__ == "__main__":
    main()


    
        