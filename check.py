import spacy
from spacy.tokens import Token
from spacy.language import Language
nlp = spacy.load("en_core_web_trf")

string = "3D PRINTER DESIGN AND PRODUCTION"
string = string[0].upper() + string.lower()[1:]
doc = nlp(string)
print(string)

for token in doc:
    print(token, token.pos_, token.dep_, token.head, list(token.children))

print("---------------------------------------------")

string = "3D PRINTER PRODUCTION AND DESIGN"
string = string[0].upper() + string.lower()[1:]
doc = nlp(string)
print(string)

for token in doc:
    print(token, token.pos_, token.dep_, token.head, list(token.children))

print("---------------------------------------------")

string = "3D PRODUCTION AND PRINTER DESIGN"
string = string[0].upper() + string.lower()[1:]
doc = nlp(string)
print(string)

for token in doc:
    print(token, token.pos_, token.dep_, token.head, list(token.children))

print("---------------------------------------------")

string = "PRODUCTION AND 3D PRINTER DESIGN"
string = string[0].upper() + string.lower()[1:]
doc = nlp(string)
print(string)

for token in doc:
    print(token, token.pos_, token.dep_, token.head, list(token.children))