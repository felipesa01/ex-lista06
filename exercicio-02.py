import numpy as np
import matplotlib.pyplot as plt

# Importar os dados do arquivo csv para um array
dados_feminino = np.genfromtxt("dados_ibge.csv", # Nome do arquivo
                   dtype=int, # Tipo dos dados da coluna
                   delimiter=";", # Delimitador
                   usecols=(2), # Coluna contendo os dados de população feminina
                   skip_header=1, # Não adotar a primeira linha
                      )
dados_idades = np.genfromtxt("dados_ibge.csv", # Nome do arquivo
                   dtype=str, # Tipo dos dados da coluna
                   delimiter=";", # Delimitador
                   usecols=(0), # Coluna contendo as faixas de idade
                   skip_header=1, # Não adotar a primeira linha
                      )
eixo_valores = np.arange(1000000,10000000,1000000) # Criar um array com valores normalizados para a população

# Definição dos parâmetros do gráfico
plt.figure(figsize=(12, 12)) # Tamanho da figura

bars = plt.bar(dados_idades, dados_feminino, align='center', color='violet', linewidth=0.5, edgecolor='black') # Definição dos dados e caracteristica dos gráfico

plt.xticks(None,None, rotation=45, ha="right") # Configuração dos rótulos do eixo x
plt.yticks(eixo_valores,[x for x in range(1,10)]) # Configuração dos rótulos do eixo y

plt.xlabel("Idade") # Título do eixo x
plt.ylabel("Número de mulheres (milhões)") # Título do eixo y

plt.grid(b=True, color='lightgrey', linestyle='--', linewidth=0.5) # Configuração da grade

for bars in bars: # Laço que rotula cada barra com os respectivos valores nominais de populacao (o eixo aprensenta valores normalizados)
    yval = bars.get_height() # Altura do gráfico como referencia da posição de impressao do valor
    if yval > 900000: # Definição e avaliacao do limiar que insere o rótulo dentro ou fora da barra
        plt.text(bars.get_x() + 0.35, yval - 50000, "{:,}".format(yval), c="black" , size=8, rotation=90, va="top" ) # Rótulos dentro da barra
    else:
        plt.text(bars.get_x() + 0.35, yval + 50000, "{:,}".format(yval), c="black", size=8, ha="center", va="bottom") # Rotulos fora da barra

plt.title("Distribuição da população feminina por idade") # Título do gráfico

plt.show() # Exibir o grafico
