from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lg = LexerGenerator()

    def _add_tokens(self):
        self.lg.add('LIFE_IS', r'life is less than')
        self.lg.add('START_PROGRAM', r'Hollownest is infected')
        self.lg.add('PROGRAM_END', r'You became the void')
        self.lg.add('VARIABLES_DECLARATION', r'souls to be sacrificed')
        self.lg.add('STATEMENT', r'\(.*?\)')
        self.lg.add('COMMA', r',')
        self.lg.add('GAME_LOOP', r'using soul')
        self.lg.add('GAME_LOOP_END', r'end using soul')
        self.lg.add('CONDITIONAL', r'full soul')
        self.lg.add('CONDITIONAL_END', r'empty soul')
        self.lg.add('VARIABLES', r':')
        self.lg.add('PURE_VESSEL', r'pure vessel')
        self.lg.add('SEALED_VESSEL', r'sealed vessel')
        self.lg.add('LIVES_AS', r'lives as')
        self.lg.add('CAUSES', r'causes')
        self.lg.add('BEING', r'being')
        self.lg.add('TO', r'to')
        self.lg.add('AND', r'&')
        self.lg.add('IF', r'if')
        self.lg.add('ACTION', r'action')
        self.lg.add('WITH', r'with souls being')
        self.lg.add('RESULTS_IN', r'results in')
        self.lg.add('VARIABLES_END', r'they became the void')
        self.lg.add('FUNCTION', r'interaction')
        self.lg.add('ENTITIES', r'entities')
        self.lg.add('DATA_TYPE', r'(player|enemy|boss|npc)(?![a-zA-Z0-9_])')
        self.lg.add('ENTITY_TYPE', r'(enemy_entity|boss_entity)(?![a-zA-Z0-9_])')
        self.lg.add('NAIL_IDENTIFIER', r'(purenail|coilednail|channellednail|sharpnail|oldnail)(?![a-zA-Z0-9_])')
        self.lg.add('SPELL_IDENTIFIER', r'(desolatedive|howlingwraiths|vengefulspirit)(?![a-zA-Z0-9_])')
        self.lg.add('DMG_TYPE', r'(playerdmg|upspelldmg|downspelldmg|horizontalspelldmg)(?![a-zA-Z0-9_])')
        self.lg.add('LIFE_CONDITION', r'(alive|dead)')
        self.lg.add('IDENTIFIER', r'[a-zA-Z][a-zA-Z0-9_]*')
        self.lg.add('DIGIT', r'[0-9]*')

        self.lg.ignore(r'\s+|\n+|\r+')  # Adicionando os caracteres de espaço em branco, nova linha e retorno de carro


    def get_lexer(self):
        self._add_tokens()
        return self.lg.build()