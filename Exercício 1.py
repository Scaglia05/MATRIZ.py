lista_carros = []
matriz_carros = [["Mercedez",250],
                 ["Volto",200],
                 ["VW",190],
                 ["GM",195],
                 ["BMW",240]]

for linha in matriz_carros:
    linha[1]
    lista_carros.append(linha[1])
    soma = 0
    for car in lista_carros:
        soma = soma + car
print(matriz_carros)
print("Terceira linha da matriz: ",matriz_carros[2])
print("Velocidade máxima do volvo:",matriz_carros[1][1])
print("A ultima marca informada é: ",matriz_carros[4][0])
print("A soma de todas as velocidades é: ",soma)


