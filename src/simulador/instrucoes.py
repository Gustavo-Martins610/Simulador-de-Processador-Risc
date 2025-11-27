class Instrucoes:

    @staticmethod
    def add(cpu, ra, rb):
        a = cpu.regs[ra]
        b = cpu.regs[rb]

        resultado = (a + b) & 0xFFFFFFFF

        cpu.flag_zero = 1 if resultado == 0 else 0
        cpu.flag_neg = 1 if (resultado & (1 << 31)) != 0 else 0
        cpu.flag_carry = 1 if a + b > 0xFFFFFFFF else 0

        sinal_a = (a >> 31) & 1
        sinal_b = (b >> 31) & 1
        sinal_r = (resultado >> 31) & 1

        cpu.flag_overflow = 1 if (sinal_a == sinal_b and sinal_r != sinal_a) else 0

        return resultado
    

    @staticmethod
    def sub(cpu, ra, rb):
        a = cpu.regs[ra]
        b = cpu.regs[rb]

        resultado = (a - b) & 0xFFFFFFFF

        cpu.flag_zero = 1 if resultado == 0 else 0
        cpu.flag_neg = 1 if (resultado & (1 << 31)) != 0 else 0
        cpu.flag_carry = 1 if a < b else 0

        sinal_a = (a >> 31) & 1
        sinal_b = (b >> 31) & 1
        sinal_r = (resultado >> 31) & 1
        cpu.flag_overflow = 1 if (sinal_a != sinal_b and sinal_r != sinal_a) else 0

        return resultado
    
    @staticmethod
    def zeros(cpu, rc):
        cpu.flag_neg = 0
        cpu.flag_zero = 1
        cpu.flag_carry = 0
        cpu.flag_overflow = 0
        return 0
    
    @staticmethod
    def xor(cpu, ra, rb):
        a = cpu.regs[ra]
        b = cpu.regs[rb]
        resultado = a ^ b

        cpu.flag_zero = 1 if resultado == 0 else 0
        cpu.flag_neg = 1 if (resultado >> 31) & 1 else 0
        cpu.flag_carry = 0
        cpu.flag_overflow = 0

        return resultado & 0xFFFFFFFF
    
    @staticmethod
    def or_(cpu, ra, rb):
        a = cpu.regs[ra]
        b = cpu.regs[rb]
        resultado = a | b

        cpu.flag_zero = 1 if resultado == 0 else 0
        cpu.flag_neg = 1 if (resultado >> 31) & 1 else 0
        cpu.flag_carry = 0
        cpu.flag_overflow = 0

        return resultado & 0xFFFFFFFF
    
    @staticmethod
    def not_(cpu, ra):
        a = cpu.regs[ra]
        resultado = (~a) & 0xFFFFFFFF

        cpu.flag_zero = 1 if resultado == 0 else 0
        cpu.flag_neg = 1 if (resultado >> 31) & 1 else 0
        cpu.flag_carry = 0
        cpu.flag_overflow = 0

        return resultado
    
    @staticmethod
    def and_(cpu, ra, rb):
        a = cpu.regs[ra]
        b = cpu.regs[rb]
        resultado = a & b

        cpu.flag_zero = 1 if resultado == 0 else 0
        cpu.flag_neg = 1 if (resultado >> 31) & 1 else 0
        cpu.flag_carry = 0
        cpu.flag_overflow = 0

        return resultado & 0xFFFFFFFF
    

    @staticmethod
    def asl(cpu, ra, rb):
        a = cpu.regs[ra]
        shift = cpu.regs[rb] & 0x1F

        resultado = (a << shift) & 0xFFFFFFFF

        cpu.flag_zero = 1 if resultado == 0 else 0
        cpu.flag_neg = 1 if (resultado >> 31) & 1 else 0
        cpu.flag_carry = 0
        cpu.flag_overflow = 0

        return resultado
    
    @staticmethod
    def asr(cpu, ra, rb):
        a = cpu.regs[ra]
        shift = cpu.regs[rb] & 0x1F
        sinal = (a >> 31) & 1

        if shift == 0:
            resultado = a
        else:
            resultado = (a >> shift) | ((0xFFFFFFFF << (32 - shift)) if sinal else 0)

        resultado &= 0xFFFFFFFF

        cpu.flag_zero = 1 if resultado == 0 else 0
        cpu.flag_neg = 1 if (resultado >> 31) & 1 else 0
        cpu.flag_carry = 0
        cpu.flag_overflow = 0

        return resultado
    
    @staticmethod
    def lsl(cpu, ra, rb):
        a = cpu.regs[ra]
        shift = cpu.regs[rb] & 0x1F

        resultado = (a << shift) & 0xFFFFFFFF

        cpu.flag_zero = 1 if resultado == 0 else 0
        cpu.flag_neg = 1 if (resultado >> 31) & 1 else 0
        cpu.flag_carry = 0
        cpu.flag_overflow = 0

        return resultado
    
    @staticmethod
    def lsr(cpu, ra, rb):
        a = cpu.regs[ra]
        shift = cpu.regs[rb] & 0x1F

        resultado = (a >> shift) & 0xFFFFFFFF

        cpu.flag_zero = 1 if resultado == 0 else 0
        cpu.flag_neg = 1 if (resultado >> 31) & 1 else 0
        cpu.flag_carry = 0
        cpu.flag_overflow = 0

        return resultado
    
    @staticmethod
    def copy(cpu, ra):
        resultado = cpu.regs[ra] & 0xFFFFFFFF

        cpu.flag_zero = 1 if resultado == 0 else 0
        cpu.flag_neg = 1 if (resultado >> 31) & 1 else 0
        cpu.flag_carry = 0
        cpu.flag_overflow = 0

        return resultado
    
    @staticmethod
    def lc_hi(cpu, const16, rc):
        atual = cpu.regs[rc]
        novo = ((const16 << 16) & 0xFFFF0000) | (atual & 0x0000FFFF)

        cpu.flag_zero = 1 if novo == 0 else 0
        cpu.flag_neg = 1 if (novo >> 31) & 1 else 0
        cpu.flag_carry = 0
        cpu.flag_overflow = 0

        return novo & 0xFFFFFFFF
    

    @staticmethod
    def lc_lo(cpu, const16, rc):
        atual = cpu.regs[rc]
        novo = (const16 & 0xFFFF) | (atual & 0xFFFF0000)

        cpu.flag_zero = 1 if novo == 0 else 0
        cpu.flag_neg = 1 if (novo >> 31) & 1 else 0
        cpu.flag_carry = 0
        cpu.flag_overflow = 0

        return novo & 0xFFFFFFFF
    

    @staticmethod
    def load(cpu, ra, rc):
        endereco = cpu.regs[ra]

        endereco = endereco & 0xFFFF

        valor = cpu.memoria[endereco]

        cpu.flag_zero = 1 if valor == 0 else 0
        cpu.flag_neg = 1 if (valor >> 31) & 1 else 0
        cpu.flag_carry = 0
        cpu.flag_overflow = 0

        return valor
    

    @staticmethod
    def store(cpu, ra, rc):
        endereco = cpu.regs[rc] & 0xFFFF
        valor = cpu.regs[ra] & 0xFFFFFFFF

        cpu.memoria[endereco] = valor

        return None
    
    @staticmethod
    def jump(cpu, endereco24):
        cpu.pc = endereco24 & 0xFFFFFF
    
    @staticmethod
    def jr(cpu, ra):
        cpu.pc = cpu.regs[ra] & 0xFFFFFFFF


    @staticmethod
    def beq(cpu, ra, rb, offset):
        if cpu.regs[ra] == cpu.regs[rb]:
            cpu.pc = cpu.pc + offset - 1

    @staticmethod
    def bne(cpu, ra, rb, offset):
        if cpu.regs[ra] != cpu.regs[rb]:
            cpu.pc = cpu.pc + offset - 1















