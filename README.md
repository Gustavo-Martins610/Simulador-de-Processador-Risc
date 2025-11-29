# 🖥️ Simulador Funcional do Processador UFLA-RISC

Este projeto implementa um simulador funcional para o processador **UFLA-RISC** de 32 bits, permitindo a execução e análise de um conjunto de instruções básicas — incluindo operações aritméticas, lógicas, de controle de fluxo, memória e manipulação de bits.

---

## 👥 Integrantes do Grupo

- **Caio Bueno Finnochio Martins**
- **Diego Alves de Oliveira**
- **Gustavo Martins de Oliveira**
- **Luiz Felipe de Souza Marques**
- **Matheus Gomes Monteiro**

---

## 🚀 Como Executar

### 1. Clone o repositório ou baixar o source code por meio da realise 1.0

```bash
git clone https://github.com/Gustavo-Martins610/ufla-risc-simulador-grupo7
```
Para baixar o source code, entre no repositório do projeto e verifique as tags
Você irá encontrar a realease 1.0

### 2. **Configure o arquivo de entrada**

No arquivo `main.py`, altere a variável `caminho` para escolher qual arquivo deseja executar.

- A pasta **bin** contém testes em arquivos binários.
- A pasta **exemplos** contém testes em linguagem de máquina `.asm`.

```python
def main():
    # 1. Definir caminhos
    caminho_assembly = "exemplos/TESTE.asm" # Arquivo de entrada em Assembly (TESTE A SER EXECUTADO)
    caminho_binario = "bin/TESTE.bin" # Arquivo de saída em Binário (recomenda-se o mesmo nome do arquivo de entrada)
```

### 3. **Execute o simulador**

```bash
python main.py
```

---

## 📂 Estrutura do Projeto

Abaixo está uma explicação clara e direta da estrutura do repositório:

### 📁 `bin/`

Diretório utilizado para armazenar arquivos binários gerados pelo assembler.

### 📁 `docs/`

Diretório opcional para documentações auxiliares.

### 📁 `exemplos/`

Contém programas de teste escritos em assembly (`.asm`).  
Esses arquivos auxiliam na validação do interpretador e do simulador.

### 📁 `src/`

Pasta com o código-fonte principal do projeto.

#### 📁 `src/interpretador/`

Contém o interpretador e o assembler.

- `assembler.py` — Converte código assembly em binário.
- `interpretador.py` — Lê arquivos `.asm` e entrega instruções já processadas ao simulador.

#### 📁 `src/simulador/`

Implementação interna do processador UFLA-RISC.

- `instrucoes.py` — Implementa o comportamento de cada instrução.
- `opcodes.py` — Define o opcode de cada instrução suportada, usado pelo assembler a fim de facilitação de acesso.
- `processador.py` — Núcleo da simulação: registradores, memória, PC e execução ciclo a ciclo.
- `unidade_controle.py` — Controla o fluxo de execução, interpretando e acionando as instruções.

### `main.py`

Arquivo principal de execução: carrega o programa, inicializa o processador e executa o ciclo completo da simulação.

---

## Licença

Projeto acadêmico sem licença comercial.
