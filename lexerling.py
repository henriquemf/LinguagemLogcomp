from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lg = LexerGenerator()

    def _add_tokens(self):
        self.lg.add('LIFE_IS', r'lifeislessthan')
        self.lg.add('VARIABLES_DECLARATION', r'souls')
        self.lg.add('STATEMENT', r'\(.*?\)')
        self.lg.add('COMMA', r',')
        self.lg.add('GAME_LOOP', r'usingsoul')
        self.lg.add('GAME_LOOP_END', r'endusingsoul')
        self.lg.add('CONDITIONAL_END', r'empty')
        self.lg.add('VARIABLES', r':')
        self.lg.add('PURE_VESSEL', r'purevessel')
        self.lg.add('SEALED_VESSEL', r'sealedvessel')
        self.lg.add('LIVES', r'lives')
        self.lg.add('CAUSES', r'causes')
        self.lg.add('BEING', r'being')
        self.lg.add('TO', r'to')
        self.lg.add('IF', r'if')
        self.lg.add('ACTION', r'action')
        self.lg.add('VARIABLES_END', r'eaten')
        self.lg.add('FUNCTION', r'interaction')
        self.lg.add('ENTITIES', r'entities')
        self.lg.add('FUNC_TYPE', r'(life_condition)(?![a-zA-Z0-9_])')
        self.lg.add('DATA_TYPE', r'(player|enemy|boss)(?![a-zA-Z0-9_])')
        self.lg.add('NAIL_IDENTIFIER', r'(purenail|coilednail|channellednail|sharpnail|oldnail)(?![a-zA-Z0-9_])')
        self.lg.add('SPELL_IDENTIFIER', r'(desolatedive|howlingwraiths|vengefulspirit)(?![a-zA-Z0-9_])')
        self.lg.add('DMG_TYPE', r'(playerdmg|upspelldmg|downspelldmg|horizontalspelldmg)(?![a-zA-Z0-9_])')
        self.lg.add('DONE', r'done')
        self.lg.add('RETURN', r'return')
        self.lg.add('USES', r'uses')
        self.lg.add('BEGIN', r'begin')
        self.lg.add('IDENTIFIER', r'[a-zA-Z][a-zA-Z0-9_]*')
        self.lg.add('DIGIT', r'[0-9]*')

        self.lg.ignore(r'\s+|\n+|\r+')  # Adicionando os caracteres de espaço em branco, nova linha e retorno de carro


    def get_lexer(self):
        self._add_tokens()
        return self.lg.build()