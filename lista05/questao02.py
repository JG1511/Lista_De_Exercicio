import math

lista_ponto1 = []
lista_ponto2 = []

print("Ponto 1")
for i in range(2):
    valor = int(input("Digite o ponto: "))
    lista_ponto1.append(valor)
print("Ponto 2")
for i in range(2):
    valor = int(input("Digite o ponto: "))
    lista_ponto2.append(valor)

tupla_ponto_1 = tuple(lista_ponto1)
tupla_ponto_2 = tuple(lista_ponto2)

distancia = ((tupla_ponto_2[0] - tupla_ponto_1[0])**2 + (tupla_ponto_2[1] - tupla_ponto_1[1])**2)
distancia_final = math.sqrt(distancia)

print(f"Distância: {distancia_final}")

