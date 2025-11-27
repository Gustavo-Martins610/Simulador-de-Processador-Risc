address 0

# 1. LCL: Carrega 0x0001 em r1
lcl r1, 1

# 2. LCH: Carrega 0xABCD nos 2 bytes mais significativos de r1
lch r1, 43981

# 3. LCL: Carrega 0x0002 em r2
lcl r2, 2

# 4. LCH: Carrega 0xFFFA nos 2 bytes mais significativos de r2
lch r2, 65530

# 5. Finaliza a execução
halt
