
from bank import value

def main():
    
    # test 0
    test_zero()
    
    # Test 20
    test_twenty()
    
    # Test 100
    test_hundred()


# test 0
def test_zero():
    assert value('hello') == '$0'
    assert value('hello , anna') == '$0'
    assert value('Hello guy') == '$0'

# test 20
def test_twenty():
    assert value('hi') == '$20'
    assert value('hi there') == '$20'
    assert value('how are you?') == '$20'

# test 100
def test_hundred():
    assert value("What's up?") == '$100'
    assert value('Morning') == '$100'
    assert value('are you crazy?!!') == '$100'    
    
 

if __name__ == '__main__':    
    main()