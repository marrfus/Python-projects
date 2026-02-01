import json

person_dict={"name":"Nazar", "age":24,"city":"Kharkiv"}

with open("personnen.json", "w",encoding="utf-8") as jsonfile:
    json.dump(person_dict, jsonfile, indent=2)

with open("personnen.json", "r",encoding="utf-8") as jsonfile:
    inhalt = json.load(jsonfile)
    print(inhalt["name"], inhalt["age"])

