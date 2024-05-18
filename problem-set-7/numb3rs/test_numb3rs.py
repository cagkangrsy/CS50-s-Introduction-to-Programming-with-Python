from numb3rs import validate

def test_length():
    assert validate('123') == False
    assert validate('123.123.123') == False
    assert validate('123.123.123.123') == True
    assert validate('123.123.123.123.123') == False

def test_outlier_numbers():
    assert validate('452.123.32.54') == False
    assert validate('146.1000.32.54') == False
    assert validate('146.68.2141.54') == False
    assert validate('146.685.71.31') == False
    assert validate('146.68.214.-921498') == False
    assert validate('-188.154.87.167') == False
    assert validate('175.15.82.117') == True

def test_string():
    assert validate('cat') == False
    assert validate('this.ip.is.incorrect') == False
