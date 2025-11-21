class UnidadeControle:

    OPCODES = {
        'ADD':   0b00000001,
        'SUB':   0b00000010,
        'ZERO':  0b00000011,
        'XOR':   0b00000100,
        'OR':    0b00000101,
        'NOT':   0b00000110,
        'AND':   0b00000111,
        'ASL':   0b00001000,
        'ASR':   0b00001001,
        'LSL':   0b00001010,
        'LSR':   0b00001011,
        'COPY':  0b00001100,
        'LC_HI': 0b00001110,
        'LC_LO': 0b00001111,
        'LOAD':  0b00010000,
        'STORE': 0b00010001,
        'JR':    0b00010011,
        'BEQ':   0b00010100,
        'BNE':   0b00010101,
        'J':     0b00010110,
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
