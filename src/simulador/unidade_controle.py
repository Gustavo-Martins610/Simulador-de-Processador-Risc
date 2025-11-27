class UnidadeControle:

    OPCODES = {
        # ALU (8 bits)
        'ADD':   0b00000001, # add
        'SUB':   0b00000010, # sub
        'ZERO':  0b00000011, # zeros
        'XOR':   0b00000100, # xor
        'OR':    0b00000101, # or
        'NOT':   0b00000110, # passnota
        'AND':   0b00000111, # and
        'ASL':   0b00001000, # Shift aritmético para a esquerda
        'ASR':   0b00001001, # Shift aritmético para a direita
        'LSL':   0b00001010, # Shift lógico à esquerda
        'LSR':   0b00001011, # Shift lógico à direita
        'COPY':  0b00001100, # copy
        
        # Constantes e Memória (8 bits)
        'LC_HI': 0b00001110, # Carrega constante de 16 bits nos 2 bytes mais significativos
        'LC_LO': 0b00001111, # Carrega constante de 16 bits nos 2 bytes menos significativos
        'LOAD':  0b00010000, # Carrega conteúdo de memória em registrador
        'STORE': 0b00010001, # Armazena conteúdo de registrador na memória
        
        # Transferência de Controle
        'JAL':   0b00010010, # jump and link
        'JR':    0b00010011, # jump register
        'BEQ':   0b00010100, # jump se igual
        'BNE':   0b00010101, # jump se diferente
        'J':     0b00010110, # jump incondicional
        
        # HALT (Condição de Término - 32 bits iguais a 1)
        'HALT':  0b11111111, # O montador vai tratar isso como 32 bits de 1s.
    }


    @staticmethod
    def extrair_opcode(instrucao_32bits: int) -> int:
        return (instrucao_32bits >> 24) & 0xFF

    @staticmethod
    def extrair_ra(instrucao_32bits: int) -> int:
        return (instrucao_32bits >> 16) & 0xFF

    @staticmethod
    def extrair_rb(instrucao_32bits: int) -> int:
        return (instrucao_32bits >> 8) & 0xFF

    @staticmethod
    def extrair_rc(instrucao_32bits: int) -> int:
        return instrucao_32bits & 0xFF

    @staticmethod
    def extrair_const16(instrucao_32bits: int) -> int:
        return (instrucao_32bits >> 8) & 0xFFFF

    @staticmethod
    def extrair_endereco24(instrucao_32bits: int) -> int:
        # Endereço de 24 bits para JUMP/JAL
        return instrucao_32bits & 0xFFFFFF
