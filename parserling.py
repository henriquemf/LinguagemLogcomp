from rply import ParserGenerator
from lexerling import lgfinal

pg = ParserGenerator(['PROGRAM', 'PROGRAM_END', 'VARIABLES_DECLARATION', 'LIFE_CONDITION',
                      'GAME_LOOP', 'GAME_LOOP_END', 'CONDITIONAL', 'CONDITIONAL_END', 'ACTION', 'WITH',
                      'VARIABLES', 'VARIABLES_END', 'FUNCTION', 'IDENTIFIER', 'COMMA', 'PURE_VESSEL', 'SEALED_VESSEL',
                      'DATA_TYPE', 'ENTITIES', 'ENTITY_TYPE', 'NAIL_IDENTIFIER', 'SPELL_IDENTIFIER', 'LIVES_AS',
                      'DMG_TYPE', 'DIGIT', 'CAUSES', 'BEING', 'TO', 'IF', 'LIFE_IS', 'RESULTS_IN', 'AND'])

@pg.production('program : PROGRAM statement_list PROGRAM_END')
def program(p):
    return p[1]

@pg.production('statement : conditional')
@pg.production('statement : variables_declaration')
@pg.production('statement : function')
@pg.production('statement : game_loop')
@pg.production('statement : action')
def statement(p):
    return p

@pg.production('statement_list : ')  # Produção para lista vazia
def statement_list_empty(p):
    return []

@pg.production('statement_list : statement')
def statement_list_single(p):
    return p

@pg.production('statement_list : statement_list statement')
def statement_list_multiple(p):
    return p

@pg.production('identifier_list : IDENTIFIER')
def identifier_list_single(p):
    return p

@pg.production('identifier_list : identifier_list COMMA IDENTIFIER')
def identifier_list_multiple(p):
    return p

@pg.production('game_loop : GAME_LOOP statement_list GAME_LOOP_END')
def game_loop(p):
    return p

@pg.production('life_condition : LIFE_CONDITION')
def life_condition(p):
    return p
@pg.production('life_check : IF IDENTIFIER LIFE_IS DIGIT RESULTS_IN life_condition')
def life_check(p):
    return p

@pg.production('damage_causing_condition : NAIL_IDENTIFIER CAUSES DMG_TYPE BEING DIGIT TO ENTITY_TYPE AND life_check')
@pg.production('damage_causing_condition : SPELL_IDENTIFIER CAUSES DMG_TYPE BEING DIGIT TO ENTITY_TYPE AND life_check')
def damage_causing_condition(p):
    return p

@pg.production('conditional : CONDITIONAL damage_causing_condition CONDITIONAL_END')
def conditional(p):
    return p

@pg.production('variables : DATA_TYPE VARIABLES IDENTIFIER LIVES_AS IDENTIFIER')
def variables(p):
    return p

@pg.production('variables_declaration : VARIABLES_DECLARATION variables VARIABLES_END')
def variables_declaration(p):
    return p

@pg.production('function : FUNCTION IDENTIFIER ENTITIES identifier_list PURE_VESSEL statement_list SEALED_VESSEL')
def function(p):
    return p

@pg.production('action : ACTION IDENTIFIER WITH identifier_list')
def action(p):
    return p

parser = pg.build()
