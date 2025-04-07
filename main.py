import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---- CRIANDO GRÁFICO

# criando alguns valores no eixo x
#x = np.array([1, 2, 3, 4])

# criando alguns valores no eixo y
#y = x*2

# label das coordenadas x e y
#plt.xlabel("Valores de x")
#plt.ylabel("Valores de y")

# executando o plot
#plt.plot(x, y)

# Formatando estilo do grafico
# marcador circular – o
# linhas pontilhadas - :
# cor verde – g (green)
# largura da linha = 3
# tamanho dos marcadores = 20

#plt.plot(x, y, "o:g", linewidth=3, markersize=20)

# criando valores no eixo x
#x = np.array([1, 2, 3, 4])

# criando valores no eixo y
#y = x*2

# novo eixo y
#y2 = x*x
#plt.xlabel("Valores de x")
#plt.xlabel("Valores de y")

# plotando dois gráficos no mesmo plano
#plt.plot(x, y, "r-", x, y2, "b--")

#x = np.array([1, 2, 3, 4])
#y = x*2
#y2 = x*x

# ---- GRÁFICOS SEPARADOS

# Plotando dois gráficos separados
#plt.subplot(1, 2, 1) #uma linha, duas colunas, posição 1
#plt.title("Linear")
#plt.plot(x, y, "r-")

#plt.subplot(1, 2, 2) #uma linha, duas colunas, posição 2
#plt.title("Exponencial")
#plt.plot(x, y2, "b--")

# ---- PONTOS

# lendo o dataset paises.csv
dfPaises = pd.read_csv("paises.csv", delimiter=";")
# extraindo somente dados dos 6 maiores países do mundo
#dfPaises2 = dfPaises.nlargest(6, "Area (sq. mi.)")
# plotando qual destes países possui a maior renda per capita
# observe que o tamanho de cada ponto ilustra o tamanho dos países
#plt.scatter(dfPaises2["Country"], dfPaises2["GDP ($ per capita)"],
#s=dfPaises2["Area (sq. mi.)"]/10000)

# ---- BARRAS

# extraindo os 5 países com maior PIB per capita (GDP) do dataset
#dfBiggestGDP = dfPaises.nlargest(5, "GDP ($ per capita)")

# pegando as Series dos países e os valores de GDP separadas
#dfBiggestGDP_country = dfBiggestGDP["Country"]
#dfBiggestGDP_gdp = dfBiggestGDP["GDP ($ per capita)"]

# traçando um gráfico em barras para ilustrar as diferenças
#plt.bar(dfBiggestGDP_country, dfBiggestGDP_gdp, color="green")

# ---- GRÁFICOS

#extraindo os países que não tem costa marítma
dfPaisesNoCoast = dfPaises[dfPaises["Coastline (coast/area ratio)"] == 0]
#extraindo a quantidade de países que não tem costa marítima
qtPaisesNoCoast = len(dfPaisesNoCoast)
#extraindo a quantidade de paises que tem costa marítma
qtPaisesCoast = len(dfPaises) - qtPaisesNoCoast
#traçando o gráfico em torta
plt.pie(x=[qtPaisesCoast, qtPaisesNoCoast], labels=["% Países Com Costa",
"% Países Sem Costa"], autopct="%1.1f%%")

# Exibir o gráfico
plt.show()  # Adicione essa linha para exibir o gráfico