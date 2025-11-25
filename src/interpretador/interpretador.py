class Interpretador:
    @staticmethod
    def carregar_arquivo(caminho):
        memoria_carregada = {}
        endereco_atual = 0

        try:
            with open(caminho, "rb") as f:
                primeiro_byte = f.read(1)

            if primeiro_byte:
                is_texto = all(32 <= byte <= 126 for byte in primeiro_byte)

                if is_texto:
                    with open(caminho, "r") as f:
                        for linha in f:
                            linha = linha.strip()

                            if linha == "":
                                continue

                            if linha.startswith("address"):
                                partes = linha.split()
                                if len(partes) != 2:
                                    raise ValueError(f"Diretiva inválida: {linha}")
                                endereco_atual = int(partes[1], 2)
                                continue

                            
                            if all(c in "01" for c in linha) and len(linha) == 32:
                                instrucao = int(linha, 2)
                                memoria_carregada[endereco_atual] = instrucao
                                endereco_atual += 1
                            else:
                                raise ValueError(f"Linha inválida encontrada: {linha}")
                else:
                    with open(caminho, "rb") as f:
                        while True:
                            instrucao = f.read(4)
                            if not instrucao:
                                break
                            instrucao_binaria = int.from_bytes(instrucao, byteorder='big')
                            memoria_carregada[endereco_atual] = instrucao_binaria
                            endereco_atual += 1

        except FileNotFoundError:
            raise FileNotFoundError(f"O arquivo {caminho} não foi encontrado.")
        except Exception as e:
            raise e

        return memoria_carregada
