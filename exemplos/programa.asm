# Exemplo de código assembly UFLA-RISC
# Este arquivo será lido pelo main.py, montado para bin/programa.bin
# e depois carregado pelo interpretador.

address 0

# Carrega a constante 10 no registrador r1 (10 em binário é 0000000000001010)
# lcl r1, 10
lcl r1, 10

# Carrega a constante 20 no registrador r2
# lcl r2, 20
lcl r2, 20

# Soma r1 e r2 e armazena em r3 (r3 = 10 + 20 = 30)
# add r3, r1, r2
add r3, r1, r2

# Copia o valor de r3 para r4
# copy r4, r3
copy r4, r3

# Zera o registrador r5
# zeros r5
zeros r5

# Instrução de parada
halt
