from src.simulador.unidade_controle import UnidadeControle
from src.simulador.instrucoes import Instrucoes
from src.simulador.opcodes import OPCODES

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

        self.memoria = [0] * 65536  # Memória de 64K (65536 endereços)

        self.halted = False

    def carregar_programa(self, memoria_carregada):
        """
        Carrega o programa na memória do processador
        """
        for endereco, instrucao in memoria_carregada.items():
            self.memoria[endereco] = instrucao

    def ciclo_IF(self):
        """
        Fase de busca de instrução
        """
        if self.pc >= len(self.memoria) or self.pc < 0:  # Se o PC for inválido
            self.halted = True
            print(f"Erro: PC inválido. PC = {self.pc}. Encerrando execução.")
            return
        
        self.ir = self.memoria[self.pc]
        
        # Se encontrar o HALT (32 bits 1)
        if self.ir == 0xFFFFFFFF:  
            print(f"Halt encontrado no PC = {self.pc}. Execução finalizada.")
            self.halted = True
        
        self.pc += 1  # Incrementa o PC após a busca da instrução

    def ciclo_ID(self):
        """
        Fase de decodificação de instrução
        """
        if self.halted:
            return
        
        self.opcode = UnidadeControle.extrair_opcode(self.ir)
        self.ra = UnidadeControle.extrair_ra(self.ir)
        self.rb = UnidadeControle.extrair_rb(self.ir)
        self.rc = UnidadeControle.extrair_rc(self.ir)
    
    def ciclo_EX(self):
        """
        Fase de execução
        """
        if self.halted:
            return
        
        if self.opcode == UnidadeControle.OPCODES['ADD']:
            self.resultado_alu = Instrucoes.add(self, self.ra, self.rb)
        elif self.opcode == UnidadeControle.OPCODES['SUB']:
            self.resultado_alu = Instrucoes.sub(self, self.ra, self.rb)
        elif self.opcode == UnidadeControle.OPCODES['ZERO']:
            self.resultado_alu = Instrucoes.zeros(self, self.rc)
        elif self.opcode == UnidadeControle.OPCODES['XOR']:
            self.resultado_alu = Instrucoes.xor(self, self.ra, self.rb)
        elif self.opcode == UnidadeControle.OPCODES['OR']:
            self.resultado_alu = Instrucoes.or_(self, self.ra, self.rb)
        elif self.opcode == UnidadeControle.OPCODES['NOT']:
            self.resultado_alu = Instrucoes.not_(self, self.ra)
        elif self.opcode == UnidadeControle.OPCODES['AND']:
            self.resultado_alu = Instrucoes.and_(self, self.ra, self.rb)
        elif self.opcode == UnidadeControle.OPCODES['ASL']:
            self.resultado_alu = Instrucoes.asl(self, self.ra, self.rb)
        elif self.opcode == UnidadeControle.OPCODES['ASR']:
            self.resultado_alu = Instrucoes.asr(self, self.ra, self.rb)
        elif self.opcode == UnidadeControle.OPCODES['LSL']:
            self.resultado_alu = Instrucoes.lsl(self, self.ra, self.rb)
        elif self.opcode == UnidadeControle.OPCODES['LSR']:
            self.resultado_alu = Instrucoes.lsr(self, self.ra, self.rb)
        elif self.opcode == UnidadeControle.OPCODES['COPY']:
            self.resultado_alu = Instrucoes.copy(self, self.ra)
        elif self.opcode == UnidadeControle.OPCODES['LC_HI']:
            const16 = UnidadeControle.extrair_const16(self.ir)
            self.resultado_alu = Instrucoes.lc_hi(self, const16, self.rc)
        elif self.opcode == UnidadeControle.OPCODES['LC_LO']:
            const16 = UnidadeControle.extrair_const16(self.ir)
            self.resultado_alu = Instrucoes.lc_lo(self, const16, self.rc)
        elif self.opcode == UnidadeControle.OPCODES['LOAD']:
            self.resultado_alu = Instrucoes.load(self, self.ra, self.rc)
        elif self.opcode == UnidadeControle.OPCODES['STORE']:
            Instrucoes.store(self, self.ra, self.rc)
        
        # Controle de Fluxo
        elif self.opcode == UnidadeControle.OPCODES['J']:
            endereco = UnidadeControle.extrair_endereco24(self.ir)
            Instrucoes.jump(self, endereco)
        elif self.opcode == UnidadeControle.OPCODES['JR']:
            Instrucoes.jr(self, self.ra)
        elif self.opcode == UnidadeControle.OPCODES['BEQ']:
            # O offset de 8 bits está armazenado em self.rc (bits 0-7)
            Instrucoes.beq(self, self.ra, self.rb, self.rc)
        elif self.opcode == UnidadeControle.OPCODES['BNE']:
            # O offset de 8 bits está armazenado em self.rc (bits 0-7)
            Instrucoes.bne(self, self.ra, self.rb, self.rc)

    def ciclo_WB(self):
        """
        Fase de escrita no registrador
        """
        if self.halted:
            return
        
        if hasattr(self, "resultado_alu"):
            self.regs[self.rc] = self.resultado_alu
            del self.resultado_alu

    def executar_ciclo(self):
        """
        Executa um ciclo completo de busca, decodificação, execução e escrita.
        """
        if self.halted:
            return
        
        self.ciclo_IF()
        self.dump_estado("IF")
        
        # Verifica se o PC ultrapassou o tamanho da memória ou se houve Halt no fetch
        if self.halted or self.pc >= len(self.memoria) or self.pc < 0:
            self.halted = True
            return
        
        self.ciclo_ID()
        self.dump_estado("ID")
        self.ciclo_EX()
        self.dump_estado("EX")
        self.ciclo_WB()
        self.dump_estado("WB")

    def dump_estado(self, ciclo_nome):
        """
        Imprime o estado atual do processador durante a execução.
        """
        print("\n" + "="*50)
        print(f"ESTÁGIO: {ciclo_nome}")
        print("-"*50)
        print(f"PC  = {self.pc}")
        print(f"IR  = {self.ir:032b}")
        print(f"OP  = {self.opcode:08b}")
        print()
        print("REGISTRADORES:")
        for i in range(32):
            if self.regs[i] != 0: # Dica: Só mostre registradores com valor != 0 pra limpar a tela
                print(f"R{i:02} = {self.regs[i]}")
        print()
        print("FLAGS:")
        print(f"NEG={self.flag_neg}  ZERO={self.flag_zero}  CARRY={self.flag_carry}  OVF={self.flag_overflow}")
        print("="*50)