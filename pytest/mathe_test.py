#es muss "test" am Anfang oder  "_test" am Ende des Names sein-
# in Namen des Funktions auch (am Anfang)

import pytest 
from mathe_functions import addiere, multipliziere

@pytest.mark.addition   #mit marken kan man teste gruppieren
def test_addition_positiv():
    ergebnis = addiere(5,8)
    assert ergebnis == 13

@pytest.mark.addition
def test_addition_negativ():
    ergebnis = addiere(-5,-5)
    assert ergebnis == -10

def test_multiplication_korrekt():
    assert multipliziere(5,5) == 25

def test_multiplication_mit_null():
    ergebnis = multipliziere(25,0)
    assert ergebnis == 0
