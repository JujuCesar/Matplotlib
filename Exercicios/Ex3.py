import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregando o dataset
dfSpace = pd.read_csv("space.csv", delimiter=";")

# Filtrando apenas missões da Roscosmos
df_roscosmos = dfSpace[dfSpace["Company Name"] == "Roscosmos"]

# Contando as missões de sucesso e falha
sucesso = len(df_roscosmos[df_roscosmos["Status Mission"] == "Success"])
falha = len(df_roscosmos[df_roscosmos["Status Mission"] != "Success"])

# Labels e dados para o gráfico
labels = ["Missões com Sucesso", "Missões com Falha"]
dados = [sucesso, falha]

# Cores para as fatias
cores = ["green", "red"]

# Plotando gráfico em torta
plt.figure(figsize=(6, 6))
plt.pie(dados, labels=labels, colors=cores, autopct="%1.1f%%", startangle=90)
plt.title("Missões da Roscosmos (Sucesso vs Falha)")
plt.axis("equal")  # Deixa o gráfico redondo
plt.show()
