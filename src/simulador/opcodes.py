OPCODES = {
    # ALU (8 bits)
    'add': '00000001',
    'sub': '00000010',
    'zeros': '00000011',
    'xor': '00000100',
    'or': '00000101',
    'not': '00000110', # not
    'and': '00000111',
    'asl': '00001000', # Shift aritmético para a esquerda
    'asr': '00001001', # Shift aritmético para a direita
    'lsl': '00001010', # Shift lógico à esquerda
    'lsr': '00001011', # Shift lógico à direita
    'copy': '00001100', # copy
    
    # Constantes e Memória (8 bits)
    'lch': '00001110', # Carrega constante de 16 bits nos 2 bytes mais significativos
    'lcl': '00001111', # Carrega constante de 16 bits nos 2 bytes menos significativos
    'load': '00010000', # Carrega conteúdo de memória em registrador
    'store': '00010001', # Armazena conteúdo de registrador na memória
    
    # Transferência de Controle (O PDF não deu opcodes, vou usar os próximos disponíveis)
    # Vou assumir opcodes para as instruções de controle que não estão no Apêndice B,
    # mas que são mencionadas no item 2.1.3.
    # jump and link, jump register, jump se igual, jump se diferente, jump incondicional
    'jal': '00010010', # jump and link
    'jr': '00010011', # jump register
    'beq': '00010100', # jump se igual
    'bne': '00010101', # jump se diferente
    'j': '00010110', # jump incondicional
    
    # HALT (Condição de Término - 32 bits iguais a 1)
    'halt': '11111111' # O montador vai tratar isso como 32 bits de 1s.
}
