address 0

# 1. LCL: Carrega 0x0001 em r1
lcl r1, 1

# 2. LCH: Carrega 0xF001 nos 2 bytes mais significativos de r1
lch r1, 61441

# 3. LCL: Carrega 0x0002 em r2
lcl r2, 2

# 4. LCH: Carrega 0xCC02 nos 2 bytes mais significativos de r2
lch r2, 52482

# 5. XOR: Realiza uma operação XOR entre r1 e r2 e armazena em r3
xor r3, r1, r2

# 6. OR: Realiza uma operação OR entre r1 e r2 e armazena em r4
or r4, r1, r2

# 7. NOT: Realiza uma operação NOT em r1 e armazena em r5
not r5, r1

# 8. COPY: Copia o valor de r1 para r6
copy r6, r1

# 9. LSR: Realiza um shift lógico à direita em r1 por r2 posições e armazena em r7
lsr r7, r1, r2

# 10. LCL: Carrega 0x0008 em r8
lcl r8, 8

# 11. Finaliza a execução
halt
