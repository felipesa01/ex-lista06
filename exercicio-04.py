import numpy as np
import matplotlib.pyplot as plt

# Importar os dados do arquivo csv para um array
dados_masculino = np.genfromtxt("dados_ibge.csv",  # Nome do arquivo
                    dtype=int,  # Tipo dos dados da coluna
                    delimiter=";",  # Delimitador
                    usecols=1,  # Coluna contendo os dados de população masculina
                    skip_header=1,  # Não adotar a primeira linha
                    )
dados_feminino = np.genfromtxt("dados_ibge.csv", # Nome do arquivo
                   dtype=int, # Tipo dos dados da coluna
                   delimiter=";", # Delimitador
                   usecols=2, # Coluna contendo os dados de população feminina
                   skip_header=1, # Não adotar a primeira linha
                   )
dados_idades = np.genfromtxt("dados_ibge.csv", # Nome do arquivo
                   dtype=str, # Tipo dos dados da coluna
                   delimiter=";", # Delimitador
                   usecols=0, # Coluna contendo as faixas de idade
                   skip_header=1, # Não adotar a primeira linha
                   )

eixo_valores = np.arange(1000000,10000000,1000000) # Criar um array com valores normalizados para a população

# Definição dos parâmetros do gráfico
plt.figure(figsize=(10, 12)) # Tamanho da figura

plt.subplot(121) # Definir subplot: grade 1x2, posição 1 (121)
plt.barh(dados_idades, dados_feminino, align='center', color='violet', linewidth=0.5, edgecolor='black') # Definição dos dados e caracteristica dos gráfico
plt.gca().invert_xaxis() # Inverter eixo x
plt.gca().axes.yaxis.set_visible(False) # Ocultar rótulos dos eixo y
plt.xticks(eixo_valores,[x for x in range(1,10)]) # Configuração dos rótulos do eixo x
plt.xlabel("Número de mulheres (milhões)") # Título do eixo x
plt.grid(b=True, color='lightgrey', linestyle='--', linewidth=0.5) # Configuração da grade

plt.subplot(122) # Definir subplot: grade 1x2, posição 2 (122)
plt.barh(dados_idades, dados_masculino, align='center', color='cornflowerblue', linewidth=0.5, edgecolor='black') # Definição dos dados e caracteristica dos gráfico
plt.yticks(None,None, ha="right") # Configuração dos rótulos do eixo y
plt.xticks(eixo_valores,[x for x in range(1,10)]) # Configuração dos rótulos do eixo x
plt.xlabel("Número de homens (milhões)") # Título do eixo x
plt.grid(b=True, axis="x", color='lightgrey', linestyle='--', linewidth=0.5, ) # Configuração da grade

plt.subplots_adjust(wspace=0.4) # Espaçar os subplots
plt.suptitle("Distribuição da população masculina por idade") # Título do gráfico
plt.show() # Exibir grafico