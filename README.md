# Projeto FloodFill: Mapeamento Inteligente de Terrenos

## Descrição do Projeto

O projeto **FloodFill** implementa um sistema de mapeamento inteligente projetado para robôs autônomos. A aplicação analisa um terreno, representado como um grid 2D, e utiliza o algoritmo **Flood Fill** para identificar, agrupar e colorir todas as regiões navegáveis que estão conectadas entre si.

O objetivo principal é transformar um mapa simples de "livre" ou "obstáculo" em um grid segmentado e de fácil interpretação, onde cada cor distinta representa uma área contínua e segura para a operação do robô, facilitando o planejamento de rotas e a classificação de zonas.

---

## Sobre o Algoritmo Flood Fill

O Flood Fill é um algoritmo clássico para determinar a área conectada a um determinado nó em uma matriz. A nossa implementação funciona da seguinte maneira:

1.  **Ponto de Partida**: O processo inicia em uma célula `(x, y)`. Se esta célula for navegável (valor `0`), ela é preenchida com uma nova cor (iniciando em `2`).
2.  **Expansão (Iterativa)**: Em vez de recursão, usamos uma pilha para controlar a expansão. Todos os vizinhos ortogonais (acima, abaixo, à esquerda e à direita) da célula atual que também são navegáveis (`0`) são adicionados à pilha.
3.  **Processo Contínuo**: O algoritmo retira itens da pilha e repete o processo de coloração e expansão até que a pilha fique vazia. Nesse ponto, uma região inteira foi colorida.
4.  **Mapeamento Completo**: Após colorir a primeira região, o sistema varre todo o grid em busca de qualquer outra célula que ainda tenha o valor `0`. Ao encontrar uma, ele inicia o processo de Flood Fill novamente com uma nova cor (incrementada), garantindo que todas as regiões, mesmo as desconectadas, sejam mapeadas.

### Complexidade Assintótica

Para um grid de dimensões $n \times m$:
- **Complexidade Temporal**: $O(n \times m)$. No pior caso, cada célula do grid é visitada e processada um número constante de vezes.
- **Complexidade Espacial**: $O(n \times m)$. A complexidade de espaço da nossa abordagem iterativa é determinada pelo tamanho máximo da pilha. No pior caso (um grid sem obstáculos), a pilha pode conter todas as células.

---

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x
- Bibliotecas `matplotlib` e `numpy`

### 1. Criar e ativar um ambiente virtual (Opcional, mas recomendado)

```bash
# Para Linux/macOS
python3 -m venv .venv
source .venv/bin/activate

# Para Windows
python -m venv .venv
.venv\Scripts\activate
```

### 2. Instalar as Dependências

Com o ambiente ativado, execute o comando abaixo para instalar as bibliotecas necessárias:
```bash
pip install matplotlib numpy
```

### 3. Executar o Script

Basta rodar o arquivo `Main.py` (ou o nome que você deu ao seu script principal):

```bash
python Main.py
```

O programa irá imprimir os grids inicial e final no terminal e, em seguida, exibirá as visualizações gráficas de cada etapa.

---

## Explicação do Código (`Main.py`)

O código está estruturado em funções modulares para clareza e reutilização:

- **`imprimir_grid(grid, titulo)`**: Responsável por exibir o grid formatado no terminal.
- **`desenhar_grid(grid, titulo)`**: Utiliza `matplotlib` para criar uma visualização colorida e gráfica do grid.
- **`flood_fill_iterativo(grid, x, y, nova_cor)`**: Contém a lógica central do algoritmo Flood Fill, usando uma pilha para preencher uma única região conectada.
- **`mapear_terreno_completo(grid, x, y)`**: Orquestra o processo completo, chamando o `flood_fill` para o ponto inicial e depois varrendo o grid para encontrar e colorir outras regiões.
- **`gerar_grid_aleatorio(...)`**: (Ponto Extra) Função que cria um grid de dimensões personalizadas com uma proporção definida de obstáculos, permitindo testes dinâmicos.

---

## Exemplos de Entrada e Saída

Conforme solicitado, o programa lida com diferentes configurações de terreno.

### Exemplo 1

- **Grid Inicial:**
  ```
  0  0  1  0  0
  0  1  1  0  0
  0  0  1  1  1
  1  1  0  0  0
  ```
- **Coordenadas Iniciais:** `(0, 0)`

- **Grid Final Preenchido:**
  ```
  2  2  1  3  3
  2  1  1  3  3
  2  2  1  1  1
  1  1  4  4  4
  ```

| Visualização Inicial | Visualização Final |
| :---: | :---: |
| ![image](https://github.com/user-attachments/assets/145923f7-1e49-4bf1-aef5-e625195c07dd)
 | ![image](https://github.com/user-attachments/assets/6ed02d4c-2bb2-43a0-b860-4dba9b5a61d8) |



### Exemplo 2

- **Grid Inicial:**
  ```
  0  1  0  0  1
  0  1  0  0  1
  0  1  1  1  1
  0  0  0  1  0
  ```
- **Coordenadas Iniciais:** `(0, 2)`

- **Grid Final Preenchido:**
  ```
  3  1  2  2  1
  3  1  2  2  1
  3  1  1  1  1
  3  3  3  1  4
  ```

| Visualização Inicial | Visualização Final |
| :---: | :---: |
| ![image](https://github.com/user-attachments/assets/2d5e1f66-2fbc-4be6-96ee-c2eedd2c30b3)
 | ![image](https://github.com/user-attachments/assets/cf2cd780-3680-48b6-a674-29333d41154e) |


---

## Conclusão

O projeto **FloodFill** implementa com sucesso uma solução robusta e eficiente para o problema de mapeamento de terrenos. A abordagem iterativa garante bom desempenho mesmo em grids grandes, e a lógica de varredura automática assegura que todo o terreno seja mapeado de forma completa e correta. O código é claro, bem documentado e atende a todos os requisitos fundamentais do enunciado.

### Ponto Extra

- **Gerador de Grids Aleatórios**: A funcionalidade de gerar grids aleatórios foi implementada na função `gerar_grid_aleatorio`, cumprindo um dos requisitos opcionais e facilitando a realização de testes abrangentes.

