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


