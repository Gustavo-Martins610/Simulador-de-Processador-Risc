class Interpretador:
    @staticmethod
    def carregar_arquivo(caminho):
        memoria_carregada = {}
        endereco_atual = 0

        try:
            # O montador gera um arquivo de texto com instruções binárias de 32 bits e diretivas 'address'.
            # O interpretador agora assume que o arquivo de entrada está neste formato.
            with open(caminho, "r") as f:
                for linha in f:
                    linha = linha.strip()

                    if linha == "":
                        continue

                    # Verifica se a linha começa com a diretiva 'address'
                    if linha.lower().startswith("address"):
                        partes = linha.split()
                        if len(partes) != 2:
                            raise ValueError(f"Diretiva inválida: {linha}")
                        try:
                            endereco_atual = int(partes[1], 2)  # Trata o endereço como binário
                        except ValueError:
                            raise ValueError(f"Endereço inválido na linha {linha}")
                        continue

                    # Verificar se a linha tem exatamente 32 bits
                    if all(c in "01" for c in linha) and len(linha) == 32:
                        try:
                            instrucao = int(linha, 2)
                            memoria_carregada[endereco_atual] = instrucao
                            endereco_atual += 1
                        except ValueError:
                            raise ValueError(f"Erro ao processar instrução binária: {linha}")
                    else:
                        raise ValueError(f"Linha inválida encontrada: {linha} (Deve ter exatamente 32 bits de '0' ou '1')")

        except FileNotFoundError:
            raise FileNotFoundError(f"O arquivo {caminho} não foi encontrado.")
        except Exception as e:
            raise e

        return memoria_carregada