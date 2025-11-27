import re
from src.simulador.opcodes import OPCODES

class Assembler:
    """
    Montador (Assembler) para a arquitetura UFLA-RISC.
    Converte código assembly para o formato binário de 32 bits.
    """

    @staticmethod
    def montar(caminho_assembly: str, caminho_saida_bin: str):
        """
        Lê o arquivo assembly, converte para binário e salva no arquivo de saída.
        """
        instrucoes_binarias = []
        endereco_atual = 0
        
        try:
            with open(caminho_assembly, 'r') as f:
                linhas = f.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"O arquivo assembly '{caminho_assembly}' não foi encontrado.")

        for num_linha, linha in enumerate(linhas, 1):
            linha = linha.strip()
            if not linha or linha.startswith('#'): # Ignora linhas vazias e comentários
                continue

            # Diretiva address
            if linha.lower().startswith('address'):
                try:
                    partes = linha.split()
                    if len(partes) != 2:
                        raise ValueError("Sintaxe inválida para 'address'. Esperado: address <endereço_binário>")
                    
                    # O PDF diz que o endereço é codificado em binário, mas o exemplo usa 'address 0' e 'address 1000001'.
                    # Vamos assumir que o endereço é um número decimal ou binário, e o interpretador espera binário.
                    # O interpretador.py atual espera o endereço em binário: endereco_atual = int(partes[1], 2)
                    # Para simplificar a entrada do usuário, vamos assumir que o usuário pode usar decimal ou binário.
                    # No entanto, o PDF diz "address end, onde end é um endereço de memória codificado em binário."
                    # Para o montador, vamos manter a saída no formato de texto binário para o interpretador.
                    
                    # Se o endereço for um número, vamos convertê-lo para binário para a saída.
                    # O interpretador atual espera um endereço em binário (string de 0s e 1s)
                    # Vamos manter a diretiva como está para a saída, mas garantir que o endereço seja válido.
                    
                    endereco_str = partes[1]
                    # Tenta interpretar como binário (como o interpretador faz)
                    try:
                        int(endereco_str, 2)
                    except ValueError:
                        # Se falhar, tenta interpretar como decimal e converte para binário
                        try:
                            endereco_decimal = int(endereco_str)
                            endereco_str = bin(endereco_decimal)[2:] # Remove '0b'
                        except ValueError:
                            raise ValueError(f"Endereço inválido na linha {num_linha}: '{endereco_str}' não é um binário ou decimal válido.")
                    
                    instrucoes_binarias.append(f"address {endereco_str}")
                    continue
                except Exception as e:
                    raise Exception(f"Erro na linha {num_linha}: {e}")

            # Instrução Assembly
            try:
                # Exemplo de instrução: add r3, r2, r1
                partes = re.split(r'[,\s]+', linha)
                mnemonico = partes[0].lower()
                operandos = partes[1:]

                if mnemonico == 'halt':
                    instrucao_binaria = '1' * 32
                elif mnemonico in OPCODES:
                    instrucao_binaria = Assembler._codificar_instrucao(mnemonico, operandos)
                else:
                    raise ValueError(f"Mnemônico desconhecido: {mnemonico}")
                
                instrucoes_binarias.append(instrucao_binaria)

            except Exception as e:
                raise Exception(f"Erro ao montar instrução na linha {num_linha}: {e}")

        # Salva o arquivo binário de saída (formato texto com binários de 32 bits)
        with open(caminho_saida_bin, 'w') as f:
            f.write('\n'.join(instrucoes_binarias) + '\n')

    @staticmethod
    def _codificar_instrucao(mnemonico: str, operandos: list) -> str:
        """
        Codifica uma instrução assembly para sua representação binária de 32 bits.
        Esta é uma implementação de exemplo e deve ser ajustada com base no `instrucoes.py` real.
        """
        
        # Mapeamento de registradores (r0 a r31) para binário de 8 bits
        def reg_to_bin(reg_str):
            match = re.match(r'r(\d+)', reg_str.lower())
            if not match:
                raise ValueError(f"Registrador inválido: {reg_str}")
            reg_num = int(match.group(1))
            if not 0 <= reg_num <= 31:
                raise ValueError(f"Número de registrador fora do intervalo (0-31): {reg_num}")
            return format(reg_num, '08b')

        # Obtém o opcode da instrução
        opcode = OPCODES.get(mnemonico)
        if not opcode:
            raise ValueError(f"Opcode não encontrado para o mnemônico: {mnemonico}")

        # Lógica de codificação baseada no tipo de instrução (R-type, I-type, etc.)
        # O PDF sugere um formato de 3 operandos (rc, ra, rb) para ALU, onde cada registrador tem 8 bits.
        # Total: 8 (OPCODE) + 8 (ra) + 8 (rb) + 8 (rc) = 32 bits.
        
        # Exemplo de codificação para instruções ALU (add, sub, xor, or, and, asl, asr, lsl, lsr)
        if mnemonico in ['add', 'sub', 'xor', 'or', 'and', 'asl', 'asr', 'lsl', 'lsr']:
            if len(operandos) != 3:
                raise ValueError(f"Instrução {mnemonico} requer 3 operandos (rc, ra, rb).")
            rc, ra, rb = operandos
            
            # Formato: OPCODE (31-24) | ra (23-16) | rb (15-8) | rc (7-0)
            return opcode + reg_to_bin(ra) + reg_to_bin(rb) + reg_to_bin(rc)

        # Codificação para instruções de 2 operandos (passa, passnota)
        elif mnemonico == 'not' or mnemonico == 'copy':
            if len(operandos) != 2:
                raise ValueError(f"Instrução {mnemonico} requer 2 operandos (rc, ra).")
            rc, ra = operandos
            
            # Formato: OPCODE (31-24) | ra (23-16) | 8 bits de padding (15-8) | rc (7-0)
            # O PDF para NOT (passnota) e COPY (passa) mostra apenas ra e rc.
            # O campo rb (15-8) deve ser preenchido com zeros.
            padding_rb = '0' * 8
            return opcode + reg_to_bin(ra) + padding_rb + reg_to_bin(rc)

        # Codificação para instrução ZERA
        elif mnemonico == 'zeros':
            if len(operandos) != 1:
                raise ValueError(f"Instrução {mnemonico} requer 1 operando (rc).")
            rc = operandos[0]
            
            # Formato: OPCODE (31-24) | 16 bits de padding (23-8) | rc (7-0)
            # O PDF mostra apenas rc. Os campos ra e rb devem ser preenchidos com zeros.
            padding_ra_rb = '0' * 16
            return opcode + padding_ra_rb + reg_to_bin(rc)

        # Codificação para instruções com constante (lch, lcl)
        elif mnemonico in ['lch', 'lcl']:
            if len(operandos) != 2:
                raise ValueError(f"Instrução {mnemonico} requer 2 operandos (rc, Const16).")
            rc, const16_str = operandos
            
            try:
                # Tenta converter para inteiro
                const16 = int(const16_str)
                # Verifica se está dentro do intervalo de 16 bits (0 a 65535)
                if not 0 <= const16 <= 65535:
                    raise ValueError("Constante de 16 bits fora do intervalo (0 a 65535).")
                # Converte para binário de 16 bits (zero-padded)
                const16_bin = format(const16, '016b')
            except ValueError as e:
                raise ValueError(f"Constante inválida: {const16_str}. Erro: {e}")
            
            # Formato: OPCODE (31-24) | Const16 (23-8) | rc (7-0)
            return opcode + const16_bin + reg_to_bin(rc)

        # Codificação para LOAD/STORE (load, store)
        elif mnemonico in ['load', 'store']:
            if len(operandos) != 2:
                # O PDF mostra 'load rc, ra' e 'store rc, ra' (Apêndice B.15 e B.16 - truncado, mas inferido)
                # O interpretador.py original usa ra e rc, onde ra é o endereço e rc é o registrador de destino/origem.
                # load rc, ra: rc = Mem[ra]
                # store ra, rc: Mem[rc] = ra
                # Vou seguir a sintaxe do PDF: load rc, ra (rc = destino, ra = endereço)
                # E store rc, ra (Mem[ra] = rc)
                # O interpretador.py original usa:
                # load(cpu, ra, rc): endereco = cpu.regs[ra], valor = cpu.memoria[endereco], return valor (para rc)
                # store(cpu, ra, rc): endereco = cpu.regs[rc], valor = cpu.regs[ra], cpu.memoria[endereco] = valor
                # Vou usar a sintaxe MIPS-like: load rt, offset(rs) -> load rc, ra
                # Vou manter a sintaxe do PDF: load rc, ra (rc = destino, ra = endereço)
                # E store rc, ra (Mem[ra] = rc)
                
                raise ValueError(f"Instrução {mnemonico} requer 2 operandos (rc, ra).")
            rc, ra = operandos
            
            # Formato: OPCODE (31-24) | ra (23-16) | 8 bits de padding (15-8) | rc (7-0)
            # O PDF para LOAD/STORE mostra ra e rc. O campo rb (15-8) deve ser preenchido com zeros.
            padding_rb = '0' * 8
            return opcode + reg_to_bin(ra) + padding_rb + reg_to_bin(rc)

        # Codificação para instruções de controle (JUMP/BRANCH)
        # O PDF menciona 3 codificações diferentes:
        # 1. Desvios condicionais (jeq, jne) - Formato I-type (offset)
        # 2. Desvios incondicionais (j, jal) - Formato J-type (endereço)
        # 3. Desvio por registrador (jr) - Formato R-type (registrador)

        # 1. Desvios Condicionais (jeq, jne)
        elif mnemonico in ['beq', 'bne']:
            if len(operandos) != 3:
                raise ValueError(f"Instrução {mnemonico} requer 3 operandos (ra, rb, offset).")
            ra, rb, offset_str = operandos
            
            try:
                offset = int(offset_str)
                # Offset de 16 bits (2^16 = 65536)
                if not -32768 <= offset <= 32767:
                    raise ValueError("Offset de 16 bits fora do intervalo.")
                # Converte para binário de 16 bits (complemento de dois)
                offset_bin = format(offset & 0xFFFF, '016b')
            except ValueError as e:
                raise ValueError(f"Offset inválido: {offset_str}. Erro: {e}")
            
            # Formato: OPCODE (31-24) | ra (23-16) | rb (15-8) | offset (7-0) - O PDF é vago.
            # Vou assumir o formato MIPS I-type adaptado: OPCODE (31-24) | ra (23-16) | rb (15-8) | offset (7-0)
            # O PDF diz: "codificadas de três maneiras diferentes".
            # Para jeq/jne, o PDF diz: "endereço de desvio especificado na instrução".
            # Vou assumir que o offset é de 8 bits (o que é muito pequeno) ou 16 bits (o que é mais razoável).
            # Se o formato for OPCODE (8) + ra (8) + rb (8) + offset (8), o offset é de 8 bits.
            # Se o formato for OPCODE (8) + ra (8) + offset (16), o offset é de 16 bits.
            # O PDF diz que a instrução é de 32 bits.
            # Vou assumir o formato: OPCODE (8) | ra (8) | rb (8) | offset (8) - offset de 8 bits.
            # O offset de 8 bits é muito pequeno. Vou assumir o formato: OPCODE (8) | ra (8) | offset (16) - offset de 16 bits.
            # Mas o PDF diz: "jump se igual, jump se diferente" e "codificadas de trˆes maneiras diferentes".
            # A primeira codificação é para desvios condicionais.
            # Vou assumir o formato: OPCODE (8) | ra (8) | rb (8) | offset (8) - offset de 8 bits.
            # O interpretador.py original tem: beq(cpu, ra, rb, offset)
            # Vou assumir que o offset é de 8 bits e que o campo rb é usado para o offset.
            # Formato: OPCODE (8) | ra (8) | rb (8) | offset (8)
            
            # Vou usar o formato MIPS I-type adaptado: OPCODE (8) | ra (8) | rb (8) | offset (8)
            # Onde offset é de 8 bits.
            
            if not -128 <= offset <= 127:
                raise ValueError("Offset de 8 bits fora do intervalo.")
            offset_bin = format(offset & 0xFF, '08b')
            
            return opcode + reg_to_bin(ra) + reg_to_bin(rb) + offset_bin

        # 2. Desvios Incondicionais (j, jal)
        elif mnemonico in ['j', 'jal']:
            if len(operandos) != 1:
                raise ValueError(f"Instrução {mnemonico} requer 1 operando (endereço).")
            endereco_str = operandos[0]
            
            try:
                endereco = int(endereco_str)
                # Endereço de 24 bits (32 - 8 do opcode)
                if not 0 <= endereco <= 16777215: # 2^24 - 1
                    raise ValueError("Endereço de 24 bits fora do intervalo.")
                endereco_bin = format(endereco, '024b')
            except ValueError as e:
                raise ValueError(f"Endereço inválido: {endereco_str}. Erro: {e}")
            
            # Formato: OPCODE (8) | endereço (24)
            return opcode + endereco_bin

        # 3. Desvio por Registrador (jr)
        elif mnemonico == 'jr':
            if len(operandos) != 1:
                raise ValueError(f"Instrução {mnemonico} requer 1 operando (ra).")
            ra = operandos[0]
            
            # Formato: OPCODE (8) | ra (8) | 16 bits de padding (23-8)
            padding = '0' * 16
            return opcode + reg_to_bin(ra) + padding

        # Se a instrução não foi codificada, levanta um erro
        raise NotImplementedError(f"Codificação para a instrução '{mnemonico}' não implementada.")


