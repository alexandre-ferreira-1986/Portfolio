from plates import is_valid

def main():
    
    test_max_min_char()
    
    test_two_first_letters()
    
    test_num_middle()
    
    test_zero_num()
    
    test_ponctuation()
    
    
    
def test_max_min_char():
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFGH') == False
    
def test_two_first_letters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('11') == False
        
def test_num_middle():
    assert is_valid('AAA234') == True
    assert is_valid('AAA23C') == False

def test_zero_num():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False    

def test_ponctuation():
    assert is_valid('PI3.14') == False
    assert is_valid('PI 55') == False

    
if __name__ == "__main__":  
    main()