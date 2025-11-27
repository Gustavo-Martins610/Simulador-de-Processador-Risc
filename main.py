from src.interpretador.interpretador import Interpretador
from src.interpretador.assembler import Assembler
import os
from src.simulador.processador import Processador

def main():
    # 1. Definir caminhos
    caminho_assembly = "exemplos/test_const.asm" # Arquivo de entrada em Assembly
    caminho_binario = "bin/test_const.bin" # Arquivo de saída em Binário

    # 2. Criar a pasta 'bin' se não existir
    os.makedirs(os.path.dirname(caminho_binario), exist_ok=True)

    # 3. Montar o código Assembly para Binário
    print(f"Montando o arquivo assembly: {caminho_assembly} -> {caminho_binario}")
    try:
        Assembler.montar(caminho_assembly, caminho_binario)
        print("Montagem concluída com sucesso.")
    except Exception as e:
        print(f"Erro durante a montagem: {e}")
        return # Interrompe se a montagem falhar

    # 4. Carregar o arquivo binário montado no Interpretador
    memoria = Interpretador.carregar_arquivo(caminho_binario)

    cpu = Processador()
    cpu.carregar_programa(memoria)

    print("Programa carregado. Executando...\n")

    while not cpu.halted:
        cpu.executar_ciclo()

    print("\nExecução finalizada!")

if __name__ == "__main__":
    main()
