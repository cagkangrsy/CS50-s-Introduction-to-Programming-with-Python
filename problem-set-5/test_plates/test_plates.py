from plates import is_valid

def test_length():
    assert is_valid('C') == False
    assert is_valid('CAGKAN1911') == False
    assert is_valid('CG1911') == True

def test_start_with_letter():
    assert is_valid('19CAG') == False
    assert is_valid('C19') == False
    assert is_valid('CAG') == True

def test_number_check():
    assert is_valid('CG1998') == True
    assert is_valid('CG19GS') == False
    assert is_valid('CG0') == False
    assert is_valid('CG098') == False

def test_alphanumeric():
    assert is_valid('CG.1998') == False
    assert is_valid('CAKO!') == False
    assert is_valid('CAG GRS') == False
    assert is_valid('?') == False
