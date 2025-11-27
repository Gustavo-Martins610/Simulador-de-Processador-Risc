address 0

# 1. LCL/LCH: Carrega 0x0001 em r1
lcl r1, 1

# 2. LCH: Carrega 0xABCD nos 2 bytes mais significativos de r1
lch r1, 43981

# 3. LCL: Carrega 0x0002 em r2
lcl r2, 2

# 4. LCH: Carrega 0x2702 nos 2 bytes mais significativos de r1
lch r1, 10018

# 5. Soma r1 e r2 e armazena em r3
add r3, r1, r2

# 6. Subtrai r2 de r1 e armazena em r4
sub r4, r1, r2

# 7. Finaliza a execução
halt
