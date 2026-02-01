import unittest
from mathe_functions import addiere,multipliziere

class TestMatheFunktionen(unittest.TestCase):

    def test_addition_positiv(self):
        # z1 = [2,3]
        # z2= [1,2,3,4,5,6,7,8,9]
        # result = [3,4,5,6,7,8,9,10,11,4,5,6,7,8,9,10,11,12]
        # for zahl in z1:
        #     for zahl2 in z2:
        #         for erg in result:
        #              ergebnis = addiere(zahl,zahl2)
        #              self.assertEqual(ergebnis,erg)
        #              break
        ergebnis = addiere(4,8)
        self.assertEqual(ergebnis,12)
    

    def test_addition_negativ(self):
        ergebnis = addiere(-2,-5)
        self.assertEqual(ergebnis,-7)
    
    def test_addition_gemischt(self):
        ergebnis = addiere(-5,7)
        self.assertEqual(ergebnis,2)

        # self.assertEqual(a,b)                 # Prüft, ob a ==b
        # self.assertFalse(x)                   # Prüft ob der Boolesche Wert von x False ist
        # self.assertTrue(x)                    # Prüft ob der Boolesche Wert von x True ist
        # self.assertIsNone(x)                  # prüft ob x None ist.
        # self.assertIn(a,bList)                # Prüft ob a in der Sequenz bList enthalten ist
        # self.assertRaises(Exc, func, *args)   # Prüft ob beim Aufruf von func(*args) eine Ausnahme vom 
                                                #   Type Exc ausgelöst wird.
    

if __name__ == '__main__':
    unittest.main()
       
    