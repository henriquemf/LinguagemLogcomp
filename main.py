import sys
import re

reserved_words = ['souls to be sacrificed', 'they became the void', 'empty soul', 
                  'pure vessel', 'sealed vessel', 'life is less than', 'using soul', 'end using soul', 'lives', 'causes', 'being', 'to', '&',
                  'if', 'with souls being', 'action', 'interaction', 'entities', 'player', 'enemy', 'done', 'return', 'uses',
                  'purenail', 'coilednail', 'desolatedive', 'howlingwraiths', 'playerdmg', 'upspelldmg', 'downspelldmg', 'begin']

# --------------------------------------------------------------------------------------
#                                     CLASSES NODES
# --------------------------------------------------------------------------------------

class Node():
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symbolTable):
        pass

class BinOp(Node):
    def Evaluate(self, symbolTable):
        left_value = self.children[0].Evaluate(symbolTable)
        right_value = self.children[1].Evaluate(symbolTable)

        left_value_type = left_value[0]
        right_value_type = right_value[0]

        left_value = left_value[1]

        if self.value == 'LESS_THAN':
            if left_value < right_value:
                return ("", 1)
            else:
                return ("", 0)
        else:
            raise Exception("Erro: Operador inválido")

class IntVal(Node):
    def Evaluate(self, symbolTable):
        return ("Int",int(self.value))

class NoOp(Node):
    def evaluate(self, symbolTable):
        pass 

class Identifier(Node):
    def Evaluate(self, symbolTable):
        return symbolTable.getter(self.value)
    
class Assignment(Node):
    def Evaluate(self, symbolTable):
        symbolTable.setter(self.children[0].value, self.children[1].Evaluate(symbolTable))
    
class Block(Node):  
    def Evaluate(self, symbolTable):
        for child in self.children:
            returnBlock = child.Evaluate(symbolTable)
            if returnBlock is not None:
                return returnBlock

class SymbolTable():
    def __init__(self):
        self.symbols = {}

    def getter(self, name):
        return self.symbols[name]

    def setter(self, name, value):
        if value[0] == self.symbols[name][0]:
            self.symbols[name] = value
        else:
            raise Exception("Erro: Tipos incompatíveis")

    def declare(self, name, value):
        if name not in self.symbols:
            self.symbols[name] = value
        else:
            raise Exception("Erro: Variável já declarada")
        
class FuncTable():
    symbols = {}

    def getter(name):
        return FuncTable.symbols[name]

    def setter(name, value):
        if value[0] == FuncTable.symbols[name][0]:
            FuncTable.symbols[name] = value
        else:
            raise Exception("Erro: Tipos incompatíveis")

    def declare(name, value):
        if name not in FuncTable.symbols:
            FuncTable.symbols[name] = value
        else:
            raise Exception("Erro: Variável já declarada")

class Println(Node):
    def Evaluate(self, symbolTable):
        print(self.children[0].Evaluate(symbolTable)[1])

class IfElse(Node):
    def Evaluate(self, symbolTable):
        if self.children[0].Evaluate(symbolTable)[1]:
            self.children[1].Evaluate(symbolTable)
        else:
            if len(self.children) == 3:
                self.children[2].Evaluate(symbolTable)

class GameLoop(Node):
    def Evaluate(self, symbolTable):
        while self.children[0].Evaluate(symbolTable)[1]:
            self.children[1].Evaluate(symbolTable)

class VarDecl(Node):
    def Evaluate(self, symbolTable):
            if self.value == "enemy":
                symbolTable.declare(self.children[0].value, ("enemy", self.children[1].Evaluate(symbolTable)[1]))
            elif self.value == "player":
                symbolTable.declare(self.children[0].value, ("player", self.children[1].Evaluate(symbolTable)[1]))
            else:
                raise Exception("Erro: Tipo inválido")
    
class FuncDec(Node):
    def Evaluate(self, funcTable):
        funcTable.declare(self.children[0].value, (self.value, self))

class FuncCall(Node):
    def Evaluate(self, funcTable):
        funcNode = funcTable.getter(self.value)
        symbolTableFunc = SymbolTable()
        identifier, *args, block = funcNode[1].children
        funcChildren = self.children

        if len(*args) != len(funcChildren):
            raise Exception("Erro: Número de argumentos inválido")

        for varDecl, funcChildren in zip(*args, funcChildren):
            varDecl.Evaluate(symbolTableFunc)
            symbolTableFunc.setter(varDecl.children[0].value, funcChildren.Evaluate(funcTable))

        (type, value) = block.Evaluate(symbolTableFunc)

        if type != identifier.Evaluate(funcTable)[0]:
            raise Exception("Erro: Tipo de retorno inválido")
        
        return (type, value)
    
class Return(Node):
    def Evaluate(self, symbolTable):
        return self.children[0].Evaluate(symbolTable)
    
# --------------------------------------------------------------------------------------
#                                     CLASSES GERAIS
# --------------------------------------------------------------------------------------

class PrePro:
    def filter(source):
        source = re.sub(r'#.*\n', '\n', source)
        source = re.sub(r'#.*', '', source)
        return source
    
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
class Tokenizer:

    def __init__(self, text, position):
        self.source = text
        self.position = position
        self.next = Token(None, None)
    
    def selectNext(self):
        numero = '' 
        while len(self.source) != self.position: 
            if self.source[self.position].isdigit():
                numero += self.source[self.position]
                self.position += 1

                while len(self.source) != self.position:
                    if self.source[self.position].isdigit():
                        numero += self.source[self.position]
                        self.position += 1
                    else:
                        self.next = Token('INT', numero)
                        return
    
                self.next = Token('INT', numero)
                return
            elif self.source[self.position].isalpha():
                palavra = self.source[self.position]
                self.position += 1

                while len(self.source) != self.position:
                    if self.source[self.position].isalpha() or self.source[self.position].isdigit() or self.source[self.position] == '_':
                        palavra += self.source[self.position]
                        self.position += 1
                    else:
                        if palavra in reserved_words:
                            if palavra == 'souls to be sacrificed':
                                self.next = Token('VARIABLES_DECLARATION', palavra)
                                return
                            elif palavra == 'they became the void':
                                self.next = Token('VARIABLES_END', palavra)
                                return
                            elif palavra == 'empty soul':
                                self.next = Token('CONDITIONAL_END', palavra)
                                return
                            elif palavra == 'pure vessel':
                                self.next = Token('FUNCTION_START', palavra)
                                return
                            elif palavra == 'sealed vessel':
                                self.next = Token('FUNCTION_END', palavra)
                                return
                            elif palavra == 'life is less than':
                                self.next = Token('LESS_THAN', palavra)
                                return
                            elif palavra == 'using soul':
                                self.next = Token('GAME_LOOP', palavra)
                                return
                            elif palavra == 'end using soul':
                                self.next = Token('GAME_LOOP_END', palavra)
                                return
                            elif palavra == 'lives':
                                self.next = Token('LIVES', palavra)
                                return
                            elif palavra == 'causes':
                                self.next = Token('CAUSES', palavra)
                                return
                            elif palavra == 'being':
                                self.next = Token('BEING', palavra)
                                return
                            elif palavra == 'to':
                                self.next = Token('TO', palavra)
                                return
                            elif palavra == 'if':
                                self.next = Token('IF', palavra)
                                return
                            elif palavra == 'with souls being':
                                self.next = Token('WITH', palavra)
                                return
                            elif palavra == 'action':
                                self.next = Token('FUNCTION_CALL', palavra)
                                return
                            elif palavra == 'interaction':
                                self.next = Token('FUNCTION_DECLARATION', palavra)
                                return
                            elif palavra == 'entities':
                                self.next = Token('ENTITIES', palavra)
                                return
                            elif palavra == 'player':
                                self.next = Token('PLAYER', palavra)
                                return
                            elif palavra == 'enemy':
                                self.next = Token('ENEMY', palavra)
                                return
                            elif palavra == 'purenail':
                                self.next = Token('PURENAIL', palavra)
                                return
                            elif palavra == 'coilednail':
                                self.next = Token('COILEDNAIL', palavra)
                                return
                            elif palavra == 'desolatedive':
                                self.next = Token('DESOLATEDIVE', palavra)
                                return
                            elif palavra == 'howlingwraiths':
                                self.next = Token('HOWLINGWRAITHS', palavra)
                                return
                            elif palavra == 'playerdmg':
                                self.next = Token('PLAYERDMG', palavra)
                                return
                            elif palavra == 'upspelldmg':
                                self.next = Token('UPSPELLDMG', palavra)
                                return
                            elif palavra == 'downspelldmg':
                                self.next = Token('DOWNSPELLDMG', palavra)
                                return
                            elif palavra == 'alive':
                                self.next = Token('ALIVE', palavra)
                                return
                            elif palavra == 'dead':
                                self.next = Token('DEAD', palavra)
                                return
                            elif palavra == 'done':
                                self.next = Token('DONE', palavra)
                                return
                            elif palavra == 'uses':
                                self.next = Token('USES', palavra)
                                return
                            elif palavra == 'return':
                                self.next = Token('RETURN', palavra)
                                return
                            elif palavra == 'begin':
                                self.next = Token('BEGIN', palavra)
                                return
                            else: 
                                raise Exception('Unexpected character')
                        else:
                            self.next = Token('IDEN', palavra)
                            return
                if palavra in reserved_words:
                    self.next = Token(palavra, None)
                    return
                else:
                    self.next = Token('IDEN', palavra)
                    return
            elif self.source[self.position] == ',':
                self.position += 1
                self.next = Token('COMMA', None)
                return

            elif self.source[self.position] == ':':
                self.next = Token('DC', None)
                self.position += 1
                return
            
            elif self.source[self.position] == '\n':
                self.position += 1
                self.next = Token('NEWLINE', None)
                return
            
            elif self.source[self.position] == ' ':
                self.position += 1

            else:
                raise Exception('Unexpected character')

        self.next = Token('EOF', None)
        return
    
    def watchNext(self):
        lastPos = self.position
        lastNext = self.next
        self.selectNext()
        nextToken = self.next

        self.position = lastPos
        self.next = lastNext

        return nextToken

class Parser:
    tokenizer = None

    def parseBlock(tokenizer):
        tokenizer.selectNext()
        node_block = Block(None, [])

        while tokenizer.next.type != 'EOF':
            node_block.children.append(Parser.parseStatement(tokenizer))
            tokenizer.selectNext()

        return node_block
    
    def parseBlockConditional(tokenizer):
        node_block = Block(None, [])
        tokenizer.selectNext()
        while tokenizer.next.type != 'CONDITIONAL_END':
            node_block.children.append(Parser.parseStatement(tokenizer))
            tokenizer.selectNext()
        return node_block
    
    def parseBlockGameLoop(tokenizer):
        node_block = Block(None, [])
        tokenizer.selectNext()
        while tokenizer.next.type != 'GAME_LOOP_END':
            node_block.children.append(Parser.parseStatement(tokenizer))
            tokenizer.selectNext()
        return node_block
    
    def parseBlockVariable(tokenizer):
        node_block = Block(None, [])
        tokenizer.selectNext()
        while tokenizer.next.type != 'VARIABLES_END':
            if tokenizer.next.type != 'NEWLINE':
                raise Exception('Expected NEWLINE')
            tokenizer.selectNext()
            if tokenizer.next.type != 'PLAYER' and tokenizer.next.type != 'ENEMY':
                raise Exception('Expected DATA_TYPE')
            data_type = tokenizer.next.value
            tokenizer.selectNext()
            if tokenizer.next.type != 'DC':
                raise Exception('Expected ":"')
            tokenizer.selectNext()
            if tokenizer.next.type != 'IDEN':
                raise Exception('Expected IDEN')
            identifier = tokenizer.next.value
            tokenizer.selectNext()
            if tokenizer.next.type != 'LIVES':
                raise Exception('Expected LIVES')
            tokenizer.selectNext()
            if data_type == 'player':
                node_declaration = VarDecl(data_type, [identifier, 5])
            elif data_type == 'enemy':
                if identifier == 'aspid':
                    node_declaration = VarDecl(data_type, [identifier, 15])
                elif identifier == 'hopper':
                    node_declaration = VarDecl(data_type, [identifier, 40])
                else:
                    raise Exception('Expected ASPID or HOPPER')
            node_block.children.append(node_declaration)
            tokenizer.selectNext()
        return node_block

    
    def parseStatement(tokenizer):

        # -------------------------------------------------------------------------------------------------------------
        #                                           VARIABLES_DEC PART
        # -------------------------------------------------------------------------------------------------------------

        if tokenizer.next.type == 'VARIABLES_DECLARATION':
            node_variables = Parser.parseBlockVariable(tokenizer)
            if tokenizer.next.type == 'VARIABLES_END':
                return Variables(None, [node_variables])
            else:
                raise Exception('Expected VARIABLES_END')
    
        # -------------------------------------------------------------------------------------------------------------
        #                                              FUNCDEC PART
        # -------------------------------------------------------------------------------------------------------------
            
        elif tokenizer.next.type == 'FUNCTION_DECLARATION':
            tokenizer.selectNext()
            if tokenizer.next.type == 'IDEN':
                nodeIdenFunc = Identifier(tokenizer.next.value, None)
                tokenizer.selectNext()
                if tokenizer.next.type == 'ENTITIES':
                    tokenizer.selectNext()
                    if tokenizer.next.type == 'PLAYER' or tokenizer.next.type == 'ENEMY':
                        nodeType = tokenizer.next.value
                        tokenizer.selectNext()
                        if tokenizer.next.type == 'DC':
                            tokenizer.selectNext()
                            if tokenizer.next.type == 'IDEN':
                                nodeIdenVar = Identifier(tokenizer.next.value, None)
                                nodeVarDecl = VarDecl(nodeType, [nodeIdenVar])
                                varDeclList = [nodeVarDecl]
                                tokenizer.selectNext()
                                while tokenizer.next.type == 'COMMA':
                                    tokenizer.selectNext()
                                    if tokenizer.next.type == 'PLAYER' or tokenizer.next.type == 'ENEMY':
                                        nodeType = tokenizer.next.value
                                        tokenizer.selectNext()
                                        if tokenizer.next.type == 'DC':
                                            tokenizer.selectNext()
                                            if tokenizer.next.type == 'IDEN':
                                                nodeIdenVar = Identifier(tokenizer.next.value, None)
                                                nodeVarDecl = VarDecl(nodeType, [nodeIdenVar])
                                                varDeclList.append(nodeVarDecl)
                                                tokenizer.selectNext()
                                            else:
                                                raise Exception('Expected IDEN')
                                        else:
                                            raise Exception('Expected ":"')
                                    else:
                                        raise Exception('Expected PLAYER or ENEMY')
                                if tokenizer.next.type == 'NEWLINE':
                                    if tokenizer.next.type == 'FUNCTION_START':
                                        node_block = Block(None, [])
                                        tokenizer.selectNext()
                                        while tokenizer.next.type != 'FUNCTION_END':
                                            node_block.children.append(Parser.parseStatement(tokenizer))
                                            tokenizer.selectNext()
                                        if tokenizer.next.type == 'FUNCTION_END':
                                            tokenizer.selectNext()
                                            if tokenizer.next.type == 'NEWLINE':
                                                return FuncDec(None, [nodeIdenFunc, varDeclList, node_block])
                                            else:
                                                raise Exception('Expected NEWLINE')
                                        else:
                                            raise Exception('Expected FUNCTION_END')
                                    else:
                                        raise Exception('Expected FUNCTION_START')
                                else:
                                    raise Exception('Expected NEWLINE')
                            else:
                                raise Exception('Expected IDEN')
                        else:
                            raise Exception('Expected ":"')
                    else:
                        raise Exception('Expected PLAYER or ENEMY')
                else:
                    raise Exception('Expected ENTITIES')
            else:
                raise Exception('Expected IDEN')

        # -------------------------------------------------------------------------------------------------------------
        #                                              GAMELOOP PART
        # -------------------------------------------------------------------------------------------------------------
        
        elif tokenizer.next.type == 'GAME_LOOP_START':
            tokenizer.selectNext()
            if tokenizer.next.type == 'INT':
                node_int = IntVal(tokenizer.next.value, None)
                tokenizer.selectNext()
                if tokenizer.next.type == 'NEWLINE':
                    node_gameloop = Parser.parseBlockGameLoop(tokenizer)
                    if tokenizer.next.type == 'GAME_LOOP_END':
                        return GameLoop(None, [node_int, node_gameloop])
                    else:
                        raise Exception('Expected GAME_LOOP_END')
                else:
                    raise Exception('Expected NEWLINE')
            else:
                raise Exception('Expected INT')
            
        # -------------------------------------------------------------------------------------------------------------
        #                                               CONDITIONAL PART
        # -------------------------------------------------------------------------------------------------------------
            
        elif tokenizer.next.type == 'IF':
            tokenizer.selectNext()
            if tokenizer.next.type == 'IDEN':
                nodeIden = Identifier(tokenizer.next.value, None)
                tokenizer.selectNext()
                if tokenizer.next.type == 'LESS_THAN':
                    operation = tokenizer.next.type
                    tokenizer.selectNext()
                    if tokenizer.next.type == 'INT':
                        node_int = IntVal(tokenizer.next.value, None)
                        node_less = BinOp(operation, [nodeIden, tokenizer.next.value])
                        tokenizer.selectNext()
                        if tokenizer.next.type == 'NEWLINE':
                            node_block = Parser.parseBlockConditional(tokenizer)
                            if tokenizer.next.type == 'CONDITIONAL_END':
                                return Conditional(None, [nodeIden, node_int, node_less, node_block])
                            else:
                                raise Exception('Expected CONDITIONAL_END')
                        else:
                            raise Exception('Expected NEWLINE')
                    else:
                        raise Exception('Expected INT')
                else:
                    raise Exception('Expected LESS_THAN')
            else:
                raise Exception('Expected IDEN')
            
        # -------------------------------------------------------------------------------------------------------------
        #                                               FUNCCALL PART
        # -------------------------------------------------------------------------------------------------------------
        
        elif tokenizer.next.type == 'ACTION':
            tokenizer.selectNext()
            if tokenizer.next.type == 'IDEN':
                node = Identifier(tokenizer.next.value, [])
                if tokenizer.watchNext().type == 'ENTITIES':
                    tokenizer.selectNext()
                    nodeFunc = FuncCall(node.value, [])
                    if tokenizer.watchNext().type != 'DONE':
                        while tokenizer.next.type != 'DONE':
                            nodeIden = Identifier(tokenizer.next.value, None)
                            nodeFunc.children.append(nodeIden)
                            if tokenizer.next.type != 'COMMA' and tokenizer.next.type != 'RPAREN':
                                raise Exception('Expected COMMA or RPAREN')
                        return nodeFunc
                    else:
                        tokenizer.selectNext()
                        return nodeFunc
                else:
                    return node
            else:
                raise Exception('Expected IDEN')
            
        # -------------------------------------------------------------------------------------------------------------
        #                                                 RETURN PART
        # -------------------------------------------------------------------------------------------------------------

        elif tokenizer.next.type == 'RETURN':
            tokenizer.selectNext()
            if tokenizer.next.type == 'IDEN':
                nodeIdentifier = Identifier(tokenizer.next.value, None)
                tokenizer.selectNext()
                if tokenizer.next.type == 'NEWLINE':
                    return Return(None, [nodeIdentifier])
                else:
                    raise Exception('Expected NEWLINE')
            else:
                raise Exception('Expected IDEN')
            
        # -------------------------------------------------------------------------------------------------------------
        #                                                 ATTACK PART
        # -------------------------------------------------------------------------------------------------------------
        
        elif tokenizer.next.type == 'BEGIN':
            tokenizer.selectNext()
            if tokenizer.next.type == 'IDEN':
                nodeIden = Identifier(tokenizer.next.value, None)
                tokenizer.selectNext()
                if tokenizer.next.type == 'USES':
                    tokenizer.selectNext()
                    if tokenizer.next.type == 'PURENAIL' or tokenizer.next.type == 'COILEDNAIL' or tokenizer.next.type == 'DESOLATEDIVE' or tokenizer.next.type == 'HOWLINGWRAITHS':
                        dmgType = tokenizer.next.type
                        tokenizer.selectNext()
                        if tokenizer.next.type == 'CAUSES':
                            tokenizer.selectNext()
                            if tokenizer.next.type == 'PLAYERDMG' or tokenizer.next.type == 'UPSPELLDMG' or tokenizer.next.type == 'DOWNSPELLDMG':
                                tokenizer.selectNext()
                                if tokenizer.next.type == 'BEING':
                                    tokenizer.selectNext()
                                    if tokenizer.next.type == 'INT':
                                        nodeInt = IntVal(tokenizer.next.value, None)
                                        tokenizer.selectNext()
                                        if tokenizer.next.type == 'TO':
                                            tokenizer.selectNext()
                                            if tokenizer.next.type == 'IDEN':
                                                nodeIden2 = Identifier(tokenizer.next.value, None)
                                                return Attack(None, [nodeIden, dmgType, nodeInt, nodeIden2])
                                            else:
                                                raise Exception('Expected IDEN')
                                        else:
                                            raise Exception('Expected TO')
                                    else:
                                        raise Exception('Expected INT')
                                else:
                                    raise Exception('Expected BEING')
                            else:
                                raise Exception('Expected PLAYERDMG or UPSPELLDMG or DOWNSPELLDMG')
                        else:
                            raise Exception('Expected CAUSES')
                    else:
                        raise Exception('Expected PURENAIL or COILEDNAIL or DESOLATEDIVE or HOWLINGWRAITHS')
                else:
                    raise Exception('Expected USES')
            else:
                raise Exception('Expected IDEN')
                        
        # -------------------------------------------------------------------------------------------------------------
        #                                                  NEWLINE
        # -------------------------------------------------------------------------------------------------------------
        
        elif tokenizer.next.type == 'NEWLINE':
            return NoOp(None, [])
        
        else:
            raise Exception('Expected FUNCTION or GAME_LOOP or CONDITIONAL or ACTION or RETURN or while or if or NEWLINE')
        
    def run(code):
        code = PrePro.filter(code)
        Parser.tokenizer = Tokenizer(code, 0)
        tree = Parser.parseBlock(Parser.tokenizer)
        
        if Parser.tokenizer.position  == len(Parser.tokenizer.source) and Parser.tokenizer.next.type == 'EOF':
            result = tree.Evaluate(symbolTable=SymbolTable())
            return result
        else:
            raise Exception('Expected EOF')
    
def main():
    code = open(sys.argv[1]).read()
    Parser.run(code)

if __name__ == '__main__':
    main()