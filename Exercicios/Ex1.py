import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregando o dataset
dfPaises = pd.read_csv("paises.csv", delimiter=";")

# Filtrando apenas países da América do Norte
dfAmericaNorte = dfPaises[dfPaises["Region"] == "NORTHERN AMERICA"]

# Pegando os nomes dos países, taxas de mortalidade e natalidade
paises = dfAmericaNorte["Country"]
taxa_mortalidade = dfAmericaNorte["Deathrate"]
taxa_natalidade = dfAmericaNorte["Birthrate"]

# Criando gráfico de linha
plt.figure(figsize=(12, 6))  # Define tamanho do gráfico
plt.plot(paises, taxa_mortalidade, label="Taxa de Mortalidade", marker="o", linestyle="--", color="red", markersize=8, alpha=0.8)
plt.plot(paises, taxa_natalidade, label="Taxa de Natalidade", marker="s", linestyle="-", color="blue", markersize=8, alpha=0.8)

# Personalizando o gráfico
plt.xlabel("Países da América do Norte")
plt.ylabel("Taxa por 1000 habitantes")
plt.title("Taxa de Natalidade vs. Taxa de Mortalidade - América do Norte")
plt.legend()  # Exibe a legenda
plt.grid(True)  # Adiciona grade para melhor leitura

# Exibir gráfico
plt.show()
