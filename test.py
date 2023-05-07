from lexerling import lgfinal
from parserling import parser

text = '''
Hollownest is infected

souls to be sacrificed
npc:npc1 lives as Iselda
npc:npc2 lives as Cornifer
player:hollowknight lives as HollowKnight
boss:boss1 lives as FalseKnight
enemy:enemy1 lives as Aspid
enemy:enemy2 lives as Boulder
they became the void

interaction killenemy entities knight, generalenemy
pure vessel
    full soul
        purenail causes playerdmg being 21 to enemy1 & if enemy1 life is less than 21 results in dead
    empty soul
sealed vessel

using soul
action killenemy with souls being hollowknight, enemy2
end using soul

You became the void
'''

tokens = lgfinal.lex(text)
for token in tokens:
    print(token)

try:
    result = parser.parse(tokens)
    print("Análise sintática bem-sucedida.")
except Exception as e:
    print("Erro de análise sintática:", e)
