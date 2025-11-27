# Teste de Instruções de Controle
# Objetivo: Testar JUMP incondicional e HALT

address 0

# 1. LCL: r1 = 1 (flag de teste)
lcl r1, 1

# 2. JUMP: Pula para o endereço 3 (instrução HALT)
j 3

# 3. ADD: Esta instrução deve ser pulada (r2 = r1 + r1 = 2)
add r2, r1, r1

# 4. HALT: Fim do programa
halt

# Teste de JEQ (Branch if Equal)
address 10

# 5. LCL: r3 = 5
lcl r3, 5
# 6. LCL: r4 = 5
lcl r4, 5

# 7. JEQ: Se r3 == r4, pule 2 instruções (offset 2)
# O PC atual é 12. PC + 2 = 14.
jeq r3, r4, 2

# 8. LCL: r5 = 0 (Esta instrução deve ser pulada)
lcl r5, 0

# 9. LCL: r5 = 1 (r5 deve ser 1)
lcl r5, 1

# 10. HALT
halt
