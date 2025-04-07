import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregando o dataset
dfSpace = pd.read_csv("space.csv", delimiter=";")

# Verificando o nome da coluna dos países e empresas e colunas 'Company Name' e 'Location'

# Filtrando apenas EUA e CHINA
df_usa = dfSpace[dfSpace["Location"].str.contains("USA")]
df_china = dfSpace[dfSpace["Location"].str.contains("China")]

# Pegando empresas únicas de cada país
empresas_usa = df_usa["Company Name"].drop_duplicates()
empresas_china = df_china["Company Name"].drop_duplicates()

# Contando o número de empresas diferentes
qt_empresas = [len(empresas_usa), len(empresas_china)]
paises = ["EUA", "CHINA"]

# Plotando o gráfico
plt.figure(figsize=(8, 5))
plt.bar(paises, qt_empresas, color=["blue", "red"])
plt.title("Nº de Empresas Espaciais por País (EUA vs China)")
plt.xlabel("País")
plt.ylabel("Quantidade de Empresas Diferentes")

# Exibindo os valores nas barras
for i, valor in enumerate(qt_empresas):
    plt.text(i, valor + 0.3, str(valor), ha="center", fontsize=12)

plt.tight_layout()
plt.show()
