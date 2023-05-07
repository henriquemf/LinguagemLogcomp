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
purenail causes playerdmg being 21 to enemy1 & if enemy1 life is less than 21 results in dead
empty soul
You became the void
"""


lexer = Lexer().get_lexer()
tokens = lexer.lex(text)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens)