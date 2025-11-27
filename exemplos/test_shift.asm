address 0

# 1. LCL: Carrega 0x0001 em r1
lcl r1, 1

# 2. LCH: Carrega 0x2001 nos 2 bytes mais significativos de r1
lch r1, 8193

# 3. LCL: Carrega 0x0002 em r2
lcl r2, 2

# 4. LCH: Carrega 0x0102 nos 2 bytes mais significativos de r2
lch r2, 258

# 5. ASL: Realiza um shift aritmético à esquerda em r1 por r2 posições e armazena em r3
asl r3, r1, r2

# 6. LSR: Realiza um shift lógico à direita em r1 por r2 posições e armazena em r4
lsr r4, r1, r2

# 7. LCL: Carrega 0x0005 em r5
lcl r5, 5

# 8. LCH: Carrega 0x0106 nos 2 bytes mais significativos de r5
lch r5, 262

# 9. Finaliza a execução
halt
