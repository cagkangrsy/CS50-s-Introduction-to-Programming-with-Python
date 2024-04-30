from bank import value

def test_value():
    assert value('hello') == 0
    assert value('HELLO') == 0
    assert value('hi, how are you?') == 20
    assert value('HI, HOW ARE YOU?') == 20
    assert value('good morning') == 100
    assert value('GOOD MORNING') == 100
