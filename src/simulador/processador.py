from src.simulador.unidade_controle import UnidadeControle
from src.simulador.instrucoes import Instrucoes
from src.simulador.unidade_controle import UnidadeControle


class Processador:
    def __init__(self):
        self.regs = [0] * 32
        
        self.flag_neg = 0
        self.flag_zero = 0
        self.flag_carry = 0
        self.flag_overflow = 0

        self.opcode = 0
        self.ra = 0
        self.rb = 0
        self.rc = 0


        self.pc = 0
        self.ir = 0

        self.memoria = [0] * 65536

        self.halted = False

    def carregar_programa(self, memoria_carregada):
        
        for endereco, instrucao in memoria_carregada.items():
            self.memoria[endereco] = instrucao

    def ciclo_IF(self):
        
        self.ir = self.memoria[self.pc]
        self.pc += 1

    def ciclo_ID(self):

        self.opcode = UnidadeControle.extrair_opcode(self.ir)
        self.ra = UnidadeControle.extrair_ra(self.ir)
        self.rb = UnidadeControle.extrair_rb(self.ir)
        self.rc = UnidadeControle.extrair_rc(self.ir)
        
        pass
    
    def ciclo_EX(self):
        if self.opcode == UnidadeControle.OPCODES['ADD']: self.resultado_alu = Instrucoes.add(self, self.ra, self.rb)

        elif self.opcode == UnidadeControle.OPCODES['SUB']: self.resultado_alu = Instrucoes.sub(self, self.ra, self.rb)

        elif self.opcode == UnidadeControle.OPCODES['ZERO']: self.resultado_alu = Instrucoes.zeros(self, self.rc)

        elif self.opcode == UnidadeControle.OPCODES['XOR']: self.resultado_alu = Instrucoes.xor(self, self.ra, self.rb)

        elif self.opcode == UnidadeControle.OPCODES['OR']: self.resultado_alu = Instrucoes.or_(self, self.ra, self.rb)

        elif self.opcode == UnidadeControle.OPCODES['NOT']: self.resultado_alu = Instrucoes.not_(self, self.ra)

        elif self.opcode == UnidadeControle.OPCODES['AND']: self.resultado_alu = Instrucoes.and_(self, self.ra, self.rb)

        elif self.opcode == UnidadeControle.OPCODES['ASL']: self.resultado_alu = Instrucoes.asl(self, self.ra, self.rb)

        elif self.opcode == UnidadeControle.OPCODES['ASR']: self.resultado_alu = Instrucoes.asr(self, self.ra, self.rb)

        elif self.opcode == UnidadeControle.OPCODES['LSL']: self.resultado_alu = Instrucoes.lsl(self, self.ra, self.rb)

        elif self.opcode == UnidadeControle.OPCODES['LSR']: self.resultado_alu = Instrucoes.lsr(self, self.ra, self.rb)

        elif self.opcode == UnidadeControle.OPCODES['COPY']: self.resultado_alu = Instrucoes.copy(self, self.ra)

        elif self.opcode == UnidadeControle.OPCODES['LC_HI']:
            const16 = UnidadeControle.extrair_const16(self.ir)
            self.resultado_alu = Instrucoes.lc_hi(self, const16, self.rc)

        elif self.opcode == UnidadeControle.OPCODES['LC_LO']:
            const16 = UnidadeControle.extrair_const16(self.ir)
            self.resultado_alu = Instrucoes.lc_lo(self, const16, self.rc)

        elif self.opcode == UnidadeControle.OPCODES['LOAD']: self.resultado_alu = Instrucoes.load(self, self.ra, self.rc)

        elif self.opcode == UnidadeControle.OPCODES['STORE']: 
            Instrucoes.store(self, self.ra, self.rc)
            if hasattr(self, "resultado_alu"): 
                del self.resultado_alu

        elif self.opcode == UnidadeControle.OPCODES['J']: 
            endereco = UnidadeControle.extrair_endereco24(self.ir)
            self.pc = endereco
            Instrucoes.jump(self, endereco)

        elif self.opcode == UnidadeControle.OPCODES['JAL']:
            endereco = UnidadeControle.extrair_endereco24(self.ir)
            Instrucoes.jal(self, endereco)

        elif self.opcode == UnidadeControle.OPCODES['JR']:
            self.pc = self.regs[self.ra]
            Instrucoes.jr(self, self.ra)

        elif self.opcode == UnidadeControle.OPCODES['BEQ']:
            offset = UnidadeControle.extrair_rc(self.ir)
            if self.regs[self.ra] == self.regs[self.rb]:
                self.pc += offset
            Instrucoes.beq(self, self.ra, self.rb, offset)
        
        elif self.opcode == UnidadeControle.OPCODES['BNE']:
            offset = UnidadeControle.extrair_rc(self.ir)
            if self.regs[self.ra] == self.regs[self.rb]:
                self.pc += offset
            Instrucoes.bne(self, self.ra, self.rb, offset)

    def ciclo_WB(self):
        if hasattr(self, "resultado_alu"):
            self.regs[self.rc] = self.resultado_alu
            del self.resultado_alu

    def executar_ciclo(self):
        if self.halted:
            return
        
        self.ciclo_IF()
        self.dump_estado("IF")
        self.ciclo_ID()
        self.dump_estado("ID")
        self.ciclo_EX()
        self.dump_estado("EX")
        self.ciclo_WB()
        self.dump_estado("WB")
        if self.ir == 0xFFFFFFFF:
            self.halted = True

    def dump_estado(self, ciclo_nome):
        print("\n" + "="*50)
        print(f"ESTÁGIO: {ciclo_nome}")
        print("-"*50)
        print(f"PC  = {self.pc}")
        print(f"IR  = {self.ir:032b}")
        print(f"OP  = {self.opcode:08b}")
        print()
        print("REGISTRADORES:")
        for i in range(32):
            print(f"R{i:02} = {self.regs[i]}")
        print()
        print("FLAGS:")
        print(f"NEG={self.flag_neg}  ZERO={self.flag_zero}  CARRY={self.flag_carry}  OVF={self.flag_overflow}")
        print("="*50)

