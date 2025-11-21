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

    pass

    def ciclo_WB(self):
        if hasattr(self, "resultado_alu"):
            self.regs[self.rc] = self.resultado_alu
            del self.resultado_alu

    def executar_ciclo(self):
        
        if self.halted:
            return

        self.ciclo_IF()
        self.ciclo_ID()
        self.ciclo_EX()
        self.ciclo_WB()

        
        if self.ir == 0xFFFFFFFF:
            self.halted = True
