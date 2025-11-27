address 0

# 1. LCL/LCH: Carrega 0xABCD1234 em r1
lcl r1, 4660  # 0x1234
lch r1, 43981 # 0xABCD

# 2. Soma r1 e r2 e armazena em r3
add r3, r1, r2

# 3. Subtrai r2 de r1 e armazena em r4
sub r4, r1, r2

# 4. XOR r1 e r2 e armazena em r5
xor r5, r1, r2

# 5. OR r1 e r2 e armazena em r6
or r6, r1, r2

# 6. NOT r1 e armazena em r7
not r7, r1

# 7. AND r1 e r2 e armazena em r8
and r8, r1, r2

# 8. Shift aritmético à esquerda de r1 por r2 e armazena em r9
asl r9, r1, r2

# 9. Shift aritmético à direita de r1 por r2 e armazena em r10
asr r10, r1, r2

# 10. Shift lógico à esquerda de r1 por r2 e armazena em r11
lsl r11, r1, r2

# 11. Shift lógico à direita de r1 por r2 e armazena em r12
lsr r12, r1, r2

# 12. Copia o valor de r1 para r13
copy r13, r1

# 13. Armazena r1 na memória no endereço 10 (r2)
store r1, r2

# 14. Carrega o valor da memória no endereço 10 (r2) em r3
load r3, r2

# 15. Se r4 == r5, faz jump
jeq r4, r5, 2

# 16. Se r6 != r7, faz jump
jne r6, r7, 4

# 17. Jump incondicional para r8
j r8

# 18. Finaliza a execução
halt
