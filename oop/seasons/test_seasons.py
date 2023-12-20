from seasons import minutes

def main():
    test_validate_date()
    
def test_validate_date():
    assert minutes(2000,1,1) == ('Twelve million, six hundred five thousand, seven hundred sixty minutes')
    assert minutes(2023,1,5) == ('Five hundred two thousand, five hundred sixty minutes')

if __name__ == "__main__":
    main()