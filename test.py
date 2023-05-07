from lexerling import lgfinal
from parserling import parser
from rply.errors import ParsingError

text = """
Hollownest is infected
souls to be sacrificed
npc: npc1 lives as Iselda
npc: npc2 lives as Cornifer
player: hollowknight lives as HollowKnight
boss: boss1 lives as FalseKnight
enemy: enemy1 lives as Aspid
enemy: enemy2 lives as Boulder
they became the void
full soul
purenail causes playerdmg being 21 to enemy1 & if enemy1 life is less than 21 results in dead
empty soul
You became the void
"""

tokens = lgfinal.lex(text)
tokens = list(tokens)

def token_generator(token_list):
    for token in token_list:
        yield token

# Imprima os tokens gerados
print("Tokens gerados:")
for token in tokens:
    print(token)

for i in range(1, len(tokens) + 1):
    partial_tokens = tokens[:i]
    try:
        result = parser.parse(token_generator(partial_tokens))
        print(f"Parsing successful up to token {i}: {tokens[i-1]}")
    except Exception as e:
        print(f"Parsing failed at token {i}: {tokens[i-1]}")
        print("Erro de análise sintática:", e)
        break
