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
