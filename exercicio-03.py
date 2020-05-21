import numpy as np
import matplotlib.pyplot as plt

# Importar os dados do arquivo csv para um array
dados_masculino = np.genfromtxt("dados_ibge.csv",  # Nome do arquivo
                    dtype=int,  # Tipo dos dados da coluna
                    delimiter=";",  # Delimitador
                    usecols=1,  # Coluna contendo os dados de população masculina
                    skip_header=1,  # Não adotar a primeira linha
                    )
dados_idades = np.genfromtxt("dados_ibge.csv", # Nome do arquivo
                   dtype=str, # Tipo dos dados da coluna
                   delimiter=";", # Delimitador
                   usecols=0, # Coluna contendo as faixas de idade
                   skip_header=1, # Não adotar a primeira linha
                      )
eixo_valores = np.arange(1000000,10000000,1000000) # Criar um array com valores normalizados para a população

# Definição dos parâmetros do gráfico
plt.figure(figsize=(12, 12)) # Tamanho da figura

bars = plt.barh(dados_idades, dados_masculino, align='center', color='cornflowerblue', linewidth=0.5, edgecolor='black') # Definição dos dados e caracteristica dos gráfico

plt.yticks(None,None, ha="right") # Configuração dos rótulos do eixo x
plt.xticks(eixo_valores,[x for x in range(1,10)]) # Configuração dos rótulos do eixo y

plt.ylabel("Idade") # Título do eixo x
plt.xlabel("Número de homens (milhões)") # Título do eixo y

plt.grid(b=True, color='lightgrey', linestyle='--', linewidth=0.5) # Configuração da grade

for bar in bars: # Laço que rotula cada barra com os respectivos valores nominais de populacao (o eixo aprensenta valores normalizados)
    xvalue = bar.get_width() # Posição do gráfico como referencia da posição de impressao do valor
    if xvalue > 1000000: # Definição e avaliacao do limiar que insere o rótulo dentro ou fora da barra
        plt.text(xvalue - 50000,bar.get_y()+0.25, "{:,}".format(xvalue), c="black" , size=8, ha="right") # Rótulos dentro da barra
    else:
        plt.text(xvalue + 50000, bar.get_y() + 0.25, "{:,}".format(xvalue), c="black", size=8, ha="left") # Rótulos fora da barra

plt.title("Distribuição da população masculina por idade") # Título do gráfico

plt.show() # Exibir o grafico
