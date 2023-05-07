from rply import ParserGenerator

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(['START_PROGRAM', 'PROGRAM_END', 'IDENTIFIER', 'COMMA', 'NAIL_IDENTIFIER', 'CAUSES', 
                      'DMG_TYPE', 'BEING', 'DIGIT', 'TO', 'ENTITY_TYPE', 'SPELL_IDENTIFIER', 'AND', 
                      'CONDITIONAL', 'CONDITIONAL_END', 'IF', 'LIFE_IS', 'RESULTS_IN', 'LIFE_CONDITION', 'DATA_TYPE', 'VARIABLES', 'LIVES_AS',
                      'VARIABLES_DECLARATION', 'VARIABLES_END', 'FUNCTION', 'ENTITIES', 'PURE_VESSEL', 'SEALED_VESSEL',
                      'GAME_LOOP', 'GAME_LOOP_END','ACTION', 'WITH',
                      ])

    def parse(self):
        @self.pg.production('program : START_PROGRAM statement_list PROGRAM_END')
        def program(p):
            return p[1]

        @self.pg.production('statement_list : statement')
        def statement_list_single(p):
            return [p[0]]

        @self.pg.production('statement_list : statement statement_list')
        def statement_list_multiple(p):
            return [p[0]] + p[1]

        @self.pg.production('statement : conditional')
        @self.pg.production('statement : variables_declaration')
        @self.pg.production('statement : function')
        @self.pg.production('statement : game_loop')
        @self.pg.production('statement : action')
        def statement(p):
            return p[0]

        @self.pg.production('identifier_list : IDENTIFIER')
        def identifier_list_single(p):
            return [p[0].getstr()]

        @self.pg.production('identifier_list : IDENTIFIER COMMA identifier_list')
        def identifier_list_multiple(p):
            return [p[0].getstr()] + p[2]

        @self.pg.production('damage_causing_condition : NAIL_IDENTIFIER CAUSES DMG_TYPE BEING DIGIT TO ENTITY_TYPE')
        @self.pg.production('damage_causing_condition : SPELL_IDENTIFIER CAUSES DMG_TYPE BEING DIGIT TO ENTITY_TYPE')
        @self.pg.production('damage_causing_condition : NAIL_IDENTIFIER CAUSES DMG_TYPE BEING DIGIT TO ENTITY_TYPE AND life_check')
        @self.pg.production('damage_causing_condition : SPELL_IDENTIFIER CAUSES DMG_TYPE BEING DIGIT TO ENTITY_TYPE AND life_check')
        def damage_causing_condition(p):
            return p

        @self.pg.production('conditional : CONDITIONAL damage_causing_condition CONDITIONAL_END')
        def conditional(p):
            return p[1]

        @self.pg.production('life_check : IF IDENTIFIER LIFE_IS DIGIT RESULTS_IN LIFE_CONDITION')
        def life_check(p):
            return p
        
        @self.pg.production('variables : DATA_TYPE VARIABLES IDENTIFIER LIVES_AS IDENTIFIER')
        def variables(p):
            return p

        @self.pg.production('variables_list : variables')
        def variables_list_single(p):
            return [p[0]]

        @self.pg.production('variables_list : variables variables_list')
        def variables_list_multiple(p):
            return [p[0]] + p[1]

        @self.pg.production('variables_declaration : VARIABLES_DECLARATION variables_list VARIABLES_END')
        def variables_declaration(p):
            return p

        @self.pg.production('function : FUNCTION IDENTIFIER ENTITIES identifier_list PURE_VESSEL statement_list SEALED_VESSEL')
        def function(p):
            return p

        @self.pg.production('game_loop : GAME_LOOP statement_list GAME_LOOP_END')
        def game_loop(p):
            return p

        @self.pg.production('action : ACTION IDENTIFIER WITH identifier_list')
        def action(p):
            return p

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()