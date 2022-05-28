import main


def test_add():
    assert main.add(3, 4) == 7
    assert main.add(3.5, 4) == 7
    assert main.add(3.9, 4) == 7
    assert main.add(3.9, 4.1) == 8


def test_to_sentence():
    assert main.to_sentence('apple') == 'Apple.'
    assert main.to_sentence('Apple trees') == 'Apple trees.'
    assert main.to_sentence('Apple trees.') == 'Apple trees.'

def test_div():
    assert main.div(8, 2) == 4
    assert main.div(16, 4) == 4
    assert main.div(20, 5) == 4

def test_pow():
    assert main.pow(2, 2) == 4
    assert main.pow(2, 3) == 8
    assert main.pow(2, 4) == 16