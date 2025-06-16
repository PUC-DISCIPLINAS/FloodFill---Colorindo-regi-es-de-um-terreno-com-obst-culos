import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import random

def imprimir_grid(grid, titulo="Grid"):
    """
    Imprime o grid no terminal de forma legível.
    
    Args:
        grid (list[list[int]]): O grid a ser impresso.
        titulo (str): O título a ser exibido acima do grid.
    """
    print(f"--- {titulo} ---")
    if not grid or not grid[0]:
        print("Grid vazio.")
        return
    for linha in grid:
        print(" ".join(f"{celula:<2}" for celula in linha))
    print("-" * (len(grid[0]) * 3))

def desenhar_grid(grid, titulo="Visualização Gráfica do Grid"):
    """
    Desenha o grid usando matplotlib, com cores personalizadas.

    Args:
        grid (list[list[int]]): O grid a ser desenhado.
        titulo (str): O título do gráfico.
    """
    if not grid or not grid[0]:
        print("Não é possível desenhar um grid vazio.")
        return

    cores = ['#FFFFFF', '#000000', '#FF0000', '#FFA500', '#FFFF00', 
             '#00FF00', '#0000FF', '#4B0082', '#EE82EE', '#A52A2A',
             '#00FFFF', '#FF00FF']
    
    max_val = np.max(grid) if grid else 0
    num_cores_necessarias = max_val + 1
    cores_disponiveis = cores * (num_cores_necessarias // len(cores) + 1)

    bounds = list(range(num_cores_necessarias + 1))
    cmap = mcolors.ListedColormap(cores_disponiveis[:num_cores_necessarias])
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(grid, cmap=cmap, norm=norm)
    ax.set_title(titulo)
    ax.set_xticks([])
    ax.set_yticks([])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            valor = grid[i][j]
            cor_texto = 'black' if valor in [0, 4, 5, 10] else 'white'
            ax.text(j, i, str(valor), ha='center', va='center', color=cor_texto, fontweight='bold')
    
    plt.show()

def flood_fill_iterativo(grid, x, y, nova_cor):
    """
    Preenche uma região conectada usando o algoritmo Flood Fill de forma iterativa.
    """
    n_linhas = len(grid)
    n_colunas = len(grid[0])
    
    cor_original = grid[x][y]
    if cor_original == nova_cor:
        return

    pilha = [(x, y)]

    while pilha:
        linha, coluna = pilha.pop()

        if grid[linha][coluna] == cor_original:
            grid[linha][coluna] = nova_cor
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nova_linha, nova_coluna = linha + dx, coluna + dy
                if 0 <= nova_linha < n_linhas and 0 <= nova_coluna < n_colunas and grid[nova_linha][nova_coluna] == cor_original:
                    pilha.append((nova_linha, nova_coluna))

def mapear_terreno_completo(grid, x_inicial, y_inicial):
    """
    Orquestra o mapeamento completo do terreno.
    """
    grid_mapeado = [list(linha) for linha in grid]
    n_linhas = len(grid_mapeado)
    n_colunas = len(grid_mapeado[0])
    
    cor_atual = 2

    if 0 <= x_inicial < n_linhas and 0 <= y_inicial < n_colunas and grid_mapeado[x_inicial][y_inicial] == 0:
        flood_fill_iterativo(grid_mapeado, x_inicial, y_inicial, cor_atual)
        cor_atual += 1

    for i in range(n_linhas):
        for j in range(n_colunas):
            if grid_mapeado[i][j] == 0:
                flood_fill_iterativo(grid_mapeado, i, j, cor_atual)
                cor_atual += 1
    
    return grid_mapeado

def gerar_grid_aleatorio(n_linhas, n_colunas, proporcao_obstaculos=0.3):
    """
    Gera um grid aleatório com uma certa proporção de obstáculos.

    Args:
        n_linhas (int): Número de linhas do grid.
        n_colunas (int): Número de colunas do grid.
        proporcao_obstaculos (float): Proporção de células que serão obstáculos (entre 0 e 1).

    Returns:
        list[list[int]]: O grid aleatório gerado.
    """
    grid = [[0] * n_colunas for _ in range(n_linhas)]
    total_celulas = n_linhas * n_colunas
    num_obstaculos = int(total_celulas * proporcao_obstaculos)

    for _ in range(num_obstaculos):
        while True:
            linha = random.randint(0, n_linhas - 1)
            coluna = random.randint(0, n_colunas - 1)
            if grid[linha][coluna] == 0:
                grid[linha][coluna] = 1
                break
    return grid

if __name__ == "__main__":
    

    print("\n\n*** EXECUTANDO EXEMPLO 1 ***")
    grid_exemplo_1 = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0]
    ]
    imprimir_grid(grid_exemplo_1, "Exemplo 1: Grid Inicial")
    grid_final_1 = mapear_terreno_completo(grid_exemplo_1, 0, 0)
    imprimir_grid(grid_final_1, "Exemplo 1: Grid Final Preenchido")
    desenhar_grid(grid_final_1, "Exemplo 1: Visualização Final")
    
    print("\n\n*** EXECUTANDO EXEMPLO 2 ***")
    grid_exemplo_2 = [
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 1, 0]
    ]
    imprimir_grid(grid_exemplo_2, "Exemplo 2: Grid Inicial")
    grid_final_2 = mapear_terreno_completo(grid_exemplo_2, 0, 2)
    imprimir_grid(grid_final_2, "Exemplo 2: Grid Final Preenchido")
    desenhar_grid(grid_final_2, "Exemplo 2: Visualização Final")
    
    print("\n\n*** EXECUTANDO EXEMPLO 3 (GRID ALEATÓRIO) ***")
    grid_aleatorio = gerar_grid_aleatorio(10, 15, proporcao_obstaculos=0.35)
    imprimir_grid(grid_aleatorio, "Exemplo 3: Grid Aleatório Inicial")
    grid_final_aleatorio = mapear_terreno_completo(grid_aleatorio, 0, 0)
    imprimir_grid(grid_final_aleatorio, "Exemplo 3: Grid Aleatório Final")
    desenhar_grid(grid_final_aleatorio, "Exemplo 3: Visualização do Grid Aleatório")
