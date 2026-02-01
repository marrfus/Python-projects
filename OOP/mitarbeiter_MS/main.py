
from mitarbeiter_hierarchie import Mitarbeiter
from entwickler import Entwickler

m1 = Mitarbeiter("Ali", 3000)
e1 = Entwickler("Maria", 3000)

print(f" Alis Gehalt nach erhöherung: {m1.erhoehe_gehalt()}")
print(f" Marias Gehalt nach erhöherung: {e1.erhoehe_gehalt()}")
# => Entwickler überschreibst keine rate, weil er von Klasse Mitarbeiter das ziehst