# Linguagem de Logíca da Computação :trophy:

## Feito por :shipit::
- Henrique Martinelli Frezzatti

## Objetivo :crossed_flags::
O objetivo desse projeto é criar uma linguagem própria, com um uso específico, do 0, crianco todas as condições necessárias para que ela tenha coisas básicas como um LOOP, condicionais, uma declaração e chamada de função.

### Lista de tarefas :heavy_check_mark::
- [x] Pensar no tema
- [x] Criar structure
- [x] Criar condicional
- [x] Criar loop
- [x] Criar declaração de função
- [x] Criar bloco de declaração de variáveis
- [x] Variáveis tipadas
- [x] Criar chamada de função
- [x] Finalizar linguagem

## EBNF da Linguagem:

```lua
PROGRAM = STRUCTURE, { STATEMENT };

STATEMENT = ( CONDITIONAL | VARIABLES | FUNCTION );

GAME_LOOP = "using soul", { STATEMENT }, "end using soul";

CONDITIONAL = "full soul", DAMAGE_CAUSING_CONDITION, "empty soul";

VARIABLES_DECLARATION = "souls to be sacrificed", { TYPED_VARIABLE }, "they became the void";

FUNCTION = "interaction", IDENTIFIER, "entities", [ TYPED_VARIABLE, { ",", TYPED_VARIABLE } ], "pure vessel", { STATEMENT }, "sealed vessel";

VARIABLES = TYPED_VARIABLE, "lives as", IDENTIFIER;

ACTION = "action", IDENTIFIER, "with souls being", "(", [ TYPED_VARIABLE, { ",", TYPED_VARIABLE } ], ")";

DAMAGE_CAUSING_CONDITION = ( NAIL_IDENTIFIER | SPELL_IDENTIFIER ) , "causes" , DMG_TYPE , "being" , DIGIT, "to", 
ENTITY_TYPE, "&", ENTITY_TYPE, "health", "less than", DIGIT, "results in", ("alive" | "dead");

LIFE_CHECK = "if", IDENTIFIER, "life is", DIGIT, "results in", LIFE_CONDITION;

IDENTIFIER = { LETTER | DIGIT };

TYPED_VARIABLE = DATA_TYPE, ":", IDENTIFIER;

DATA_TYPE = ( "player" | "enemy" | "boss" | "npc" );

ENTITY_TYPE = ( "enemy" | "boss" ), IDENTIFIER;

NAIL_IDENTIFIER = ( "purenail" | "coilednail" | "channellednail"  | "sharpnail" | "oldnail" );

SPELL_IDENTIFIER = ( "desolatedive" | "howlingwraiths" | "vengefulspirit" );

DMG_TYPE = ( "playerdmg" | "upspelldmg" | "downspelldmg" | "horizontalspelldmg" );

DIGIT = ("0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9");

LETTER = ("a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z");

STRUCTURE = "Hollownest is infected", VARIABLES_DECLARATION, PROGRAM, "You became the void";
```

## Exemplo de uso da linguagem:

```lua
HOLLOWNEST IS INFECTED

souls to be sacrificed
npc:npc1 lives as Iselda
npc:npc2 lives as Cornifer
player:hollowknight lives as Hollow Knight
boss:boss1 lives as False Knight
enemy:enemy1 lives as Aspid
enemy:enemy2 lives as Boulder
they became the void

interaction killenemy entities (knight, generalenemy)
pure vessel
    full soul
        purenail causes playerdmg being 21 to enemy1 & enemy1 health less than 21 results in dead
    empty soul
sealed vessel

using soul
action killenemy with souls being (hollowknight, enemy2)
end using soul
```
