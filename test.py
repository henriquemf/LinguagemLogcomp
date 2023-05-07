from lexerling import Lexer
from parserling import Parser
from rply.errors import ParsingError

text = """
Hollownest is infected
souls to be sacrificed
npc:npc1 lives as Iselda
npc:npc2 lives as Cornifer
player:hollowknight lives as HollowKnight
boss:boss1 lives as FalseKnight
enemy:enemy1 lives as Aspid
enemy:enemy2 lives as Boulder
they became the void
full soul
purenail causes playerdmg being 21 to enemy_entity & if enemy1 life is less than 21 results in dead
empty soul
You became the void
"""


lexer = Lexer().get_lexer()
tokens = lexer.lex(text)

pg = Parser()
pg.parse()
parser = pg.get_parser()

def token_generator(token_list):
    for token in token_list:
        print(token)
        yield token

# Remova a parte que adiciona o token de final de arquivo ($end)
tokens = list(filter(lambda t: t.gettokentype() != '$end', tokens))

try:
    result = parser.parse(token_generator(tokens))
    print("Parsing successful!")
except Exception as e:
    print("Parsing failed:")
    print("Exception:", e)

