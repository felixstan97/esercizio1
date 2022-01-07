'''class JsonArray:

    del __init__(self,resto2):
        self.resto2 = resto1
        
        
    resto1= '{'uno': 2,'tre': 'quattro'},{'uno': 6, 'tre': 'otto'} ,{'uno':5, 'tre':'sarmale'}'
        
     def _dammi(self):
        return self.resto1'''

import json

x = '{ "nome": "Luca", "cognome": "Rossi", "eta": 25}'


y = json.loads(x)

print(y)
print(y["nome"])


b = [
        {
        "nome": "Luca",
        "cognome": "Rossi", 
        "eta": 25,
        "online": False,
        "interessi": ["calcio","nuoto","basket"],
        "macchina": None
        },
        {
        "nome": "Franco",
        "cognome": "Vizzio", 
        "eta": 19,
        "online": True,
        "interessi": ["pallavolo","skteboard","sci"],
        "macchina": None
        }
    ]

m = json.dumps(b)

print(m)
print(b)


s = json.dumps(b,indent=4)
print(s)













