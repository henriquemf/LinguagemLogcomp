from rply import ParserGenerator

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(['IDENTIFIER', 'COMMA', 'NAIL_IDENTIFIER', 'CAUSES', 
                      'DMG_TYPE', 'BEING', 'DIGIT', 'TO', 'SPELL_IDENTIFIER', 
                      'CONDITIONAL_END', 'IF', 'LIFE_IS', 'DATA_TYPE', 'VARIABLES', 'LIVES',
                      'VARIABLES_DECLARATION', 'VARIABLES_END', 'FUNCTION', 'ENTITIES', 'PURE_VESSEL', 'SEALED_VESSEL',
                      'GAME_LOOP', 'GAME_LOOP_END','ACTION', 'WITH', 'DONE', 'USES', 'RETURN', 'BEGIN',
                      ])

    def parse(self):
        @self.pg.production('program : statement_list')
        def program(p):
            return p[0]

        @self.pg.production('statement_list : statement')
        def statement_list_single(p):
            return [p[0]]

        @self.pg.production('statement_list : statement statement_list')
        def statement_list_multiple(p):
            return [p[0]] + p[1]

        @self.pg.production('statement : conditional')
        @self.pg.production('statement : variables_declaration')
        @self.pg.production('statement : function')
        @self.pg.production('statement : function_call')
        @self.pg.production('statement : game_loop')
        def statement(p):
            return p[0]

        @self.pg.production('identifier_list : IDENTIFIER')
        def identifier_list_single(p):
            return [p[0].getstr()]

        @self.pg.production('identifier_list : IDENTIFIER COMMA identifier_list')
        def identifier_list_multiple(p):
            return [p[0].getstr()] + p[2]
        
        @self.pg.production('identifier_typed_list : DATA_TYPE VARIABLES IDENTIFIER')
        def identifier_typed_list_single(p):
            return [p[0].getstr(), p[2].getstr()]
        
        @self.pg.production('identifier_typed_list : DATA_TYPE VARIABLES IDENTIFIER COMMA identifier_typed_list')
        def identifier_typed_list_multiple(p):
            return [p[0].getstr(), p[2].getstr()] + p[4]
        
        @self.pg.production('inside_function_list : inside_function')
        def inside_function_list_single(p):
            return [p[0]]
        
        @self.pg.production('inside_function_list : inside_function inside_function_list')
        def inside_function_list_multiple(p):
            return [p[0]] + p[1]
        
        @self.pg.production('inside_function : attack')
        @self.pg.production('inside_function : conditional')
        @self.pg.production('inside_function : game_loop')
        def inside_function(p):
            return p[0]
        
        @self.pg.production('attack : BEGIN IDENTIFIER USES NAIL_IDENTIFIER CAUSES DMG_TYPE BEING DIGIT TO IDENTIFIER')
        @self.pg.production('attack : BEGIN IDENTIFIER USES SPELL_IDENTIFIER CAUSES DMG_TYPE BEING DIGIT TO IDENTIFIER')
        def attack(p):
            return p

        @self.pg.production('conditional : IF IDENTIFIER LIFE_IS DIGIT attack CONDITIONAL_END')
        def conditional(p):
            return p

        @self.pg.production('variables : DATA_TYPE VARIABLES IDENTIFIER LIVES')
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

        @self.pg.production('function : FUNCTION IDENTIFIER ENTITIES identifier_typed_list PURE_VESSEL inside_function_list RETURN IDENTIFIER SEALED_VESSEL')
        def function(p):
            return p

        @self.pg.production('function_call : ACTION IDENTIFIER ENTITIES identifier_list DONE')
        def function_call(p):
            return p

        @self.pg.production('game_loop : GAME_LOOP DIGIT inside_function_list DIGIT GAME_LOOP_END')
        def game_loop(p):
            return p
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()