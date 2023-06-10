from lexerling import Lexer
from parserling import Parser
from rply.errors import ParsingError

text = """
souls to be sacrificed
player:hollowknight lives
boss:boss1 lives
enemy:enemy1 lives
enemy:enemy2 lives
they became the void
if enemy1 life is less than 21
    begin hollowknight uses purenail causes playerdmg being 21 to enemy1    
empty soul
interaction teste1 entities enemy:enemy1, player:hollowknight 
pure vessel
    using soul 20
        begin hollowknight uses purenail causes playerdmg being 21 to enemy1
        begin hollowknight uses howlingwraiths causes upspelldmg being 15 to enemy1
        begin hollowknight uses desolatedive causes downspelldmg being 15 to enemy1
        5
    end using soul
    return enemy1
sealed vessel
action teste1 entities enemy1, hollowknight done
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

