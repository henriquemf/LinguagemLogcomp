from lexerling import Lexer
from parserling import Parser
from rply.errors import ParsingError

text = """
souls
player:hollowknight lives
enemy:aspid lives
eaten
if aspid lifeislessthan 21
    begin hollowknight uses purenail causes playerdmg being 21 to aspid    
empty
interaction:life_condition teste1 entities enemy:aspid, player:hollowknight 
purevessel
    usingsoul 20
        begin hollowknight uses purenail causes playerdmg being 21 to aspid
        begin hollowknight uses howlingwraiths causes upspelldmg being 15 to aspid
        begin hollowknight uses desolatedive causes downspelldmg being 15 to aspid
        5
    endusingsoul
    return live_condition
sealedvessel
action teste1 entities aspid, hollowknight done
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

