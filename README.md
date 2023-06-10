# Linguagem de Logíca da Computação :trophy:

## Feito por :shipit::
- Henrique Martinelli Frezzatti

## Objetivo :crossed_flags::
O objetivo desse projeto é criar uma linguagem própria, com um uso específico, do 0, crianco todas as condições necessárias para que ela tenha coisas básicas como um LOOP, condicionais, uma declaração e chamada de função.

## Considerações:
A linguagem criada possui algumas limitações devido ao funcionamento do jogo e da lógica apresentada. No jogo, apenas um único ataque pode ser executado de cada vez, não há como sobrepor ataques em uma única execução de comando. Dessa forma, só é permitido utilizar apenas um único ATAQUE dentro de GameLoop, visto que não é permitido no próprio jogo essa sobreposição. 

Além disso, a função possui o papel de simular um ataque com a permissão de fazer isso N vezes com a utilização do GameLoop ou somente se a vida do inimigo for menor que um certo valor utilizando o CONDITIONAL. Dessa forma, ela sempre irá retornar "ALIVE" ou "DEAD" no print final do terminal. 

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
PROGRAM = VARIABLES_DECLARATION,{ STATEMENT };

STATEMENT = ( CONDITIONAL | VARIABLES | FUNCTION );

GAME_LOOP = "usingsoul", { STATEMENT }, "endusingsoul";

CONDITIONAL = "if", IDENTIFIER, "lifeislessthan", DIGIT, ATTACK, "empty";

VARIABLES_DECLARATION = "souls", { VARIABLES }, "eaten";

FUNC_TYPE = ( "life_condition" );

FUNCTION = "interaction", ":", FUNC_TYPE, IDENTIFIER, "entities", [ IDENTIFIER, { ",", IDENTIFIER } ], "purevessel", { ATTACK },"return", IDENTIFIER, "sealedvessel";

VARIABLES = DATA_TYPE, ":", IDENTIFIER, "lives";

ACTION = "action", IDENTIFIER, "entities", [ IDENTIFIER, { ",", IDENTIFIER } ], "done";

ATTACK = "begin", IDENTIFIER, "uses", ( NAIL_IDENTIFIER | SPELL_IDENTIFIER ) , "causes" , DMG_TYPE , "being" , DIGIT, "to", IDENTIFIER;

IDENTIFIER = { LETTER | DIGIT };

DATA_TYPE = ( "player" | "enemy" | "boss" );

NAIL_IDENTIFIER = ( "purenail" | "coilednail" | "channellednail"  | "sharpnail" | "oldnail" );

SPELL_IDENTIFIER = ( "desolatedive" | "howlingwraiths" | "vengefulspirit" );

DMG_TYPE = ( "playerdmg" | "upspelldmg" | "downspelldmg" | "horizontalspelldmg" );

DIGIT = ("0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9");

LETTER = ("a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z");
```

## Exemplo de uso da linguagem:

```lua
souls
player:hollowknight lives
enemy:hopper lives
eaten
interaction:life_condition ataque1 entities enemy:enemy1, player:player1 
purevessel
    usingsoul 10
        if enemy1 lifeislessthan 10
            begin player1 uses purenail causes playerdmg being 1 to enemy1    
        empty
        begin player1 uses purenail causes playerdmg being 1 to enemy1
        5
    endusingsoul
    return enemy1
sealedvessel
action ataque1 entities hopper, hollowknight done
```
