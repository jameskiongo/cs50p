from seasons import validate_date

def main():
    test_validate_date()
    
def test_validate_date():
    assert validate_date('1988-07-03') == ('1988-07-03')
    assert validate_date('1988-7-3') == None
    assert validate_date('July 3, 1998') == None

if __name__ == "__main__":
    main()