import json
from dataclasses import dataclass,asdict


# {
#     "name": "Anna",
#     "alter": 25,
#     "verheitet": false,
#     "hobbys": ["Lesen", "sport"],
#     "adresse": {
#       "stadt": "Köln",
#       "plz": 51063
#     }
#   }

@dataclass
class Address:
    city:str
    zipcode:str

@dataclass
class Person:
    name:str
    age:int
    married:bool
    hobbies:list
    address: Address

p1= Person("Taras", 37,False,["writing", "painting"],Address("Morintsi","20210"))
p2= Person("Artem", 34, True, ["fact checking"], Address("Kyiv","01001"))

p_list=[p1,p2]

try:    
    with open("persons.json","r",encoding="utf-8") as jf:
        content = json.load(jf)
except Exception:
    content = []

for p in p_list:
    content.append(asdict(p))

with open("persons.json","w",encoding="utf-8") as jf:
    json.dump(content, jf, indent=2, ensure_ascii=False)
    