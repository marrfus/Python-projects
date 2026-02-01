from dataclasses import dataclass,asdict

@dataclass
class Hund:
    rasse:str
    grosse_cm:int
    besonderheit: str

h=Hund("Pitbull",51, "smart,stark, energisch")