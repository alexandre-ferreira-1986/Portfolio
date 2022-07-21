from CS50_07_01_seasons import check_birthday


def main():
    
    test_check_birthday()
    

def test_check_birthday():
    
    assert check_birthday('1994-01-02') == ('1998', '01', '02')
    assert check_birthday('1994-1-2') == None
    assert check_birthday('April 5, 1992') == None
    
   
if __name__ == '__main__':
    main()