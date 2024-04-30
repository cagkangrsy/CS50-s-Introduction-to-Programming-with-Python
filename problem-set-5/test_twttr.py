from twttr import shorten

def test_shorten():
    assert shorten('Cagkan') == 'Cgkn'
    assert shorten('GURSOY') == 'GRSY'
    assert shorten('cagkan, gursoy') == 'cgkn, grsy'
    assert shorten('CS50') == 'CS50'
