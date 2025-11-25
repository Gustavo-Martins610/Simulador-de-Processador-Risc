from src.interpretador.interpretador import Interpretador
from src.simulador.processador import Processador

def main():
    caminho = "binarios/teste_programa2.bin"
    #caminho = "exemplos/test_all.txt"

    memoria = Interpretador.carregar_arquivo(caminho)

    cpu = Processador()
    cpu.carregar_programa(memoria)

    print("Programa carregado. Executando...\n")

    while not cpu.halted:
        cpu.executar_ciclo()

    print("\nExecução finalizada!")

if __name__ == "__main__":
    main()
