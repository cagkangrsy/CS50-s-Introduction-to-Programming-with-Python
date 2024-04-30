from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert('4/5') == 80
    assert convert('1/200') == 0

def test_errors():
    with pytest.raises(ValueError):
         convert('45')
    with pytest.raises(ValueError):
         convert('4.5/5.5')
    with pytest.raises(ValueError):
         convert('6/3')
    with pytest.raises(ZeroDivisionError):
         convert('10/0')
def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'
    assert gauge(50) == '50%'
    assert gauge(33) == '33%'
