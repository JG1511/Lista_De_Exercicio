lista_frutas = input("Digite o nome das fruntas, utilize o espaço: ").split()
lista_vegetais = input("Digite o nome dos vegetais, utilize o espaço: ").split()

tuplas_frutas = tuple(lista_frutas)
tuplas_vegetais = tuple(lista_vegetais)

tuplas_final = (tuplas_frutas + tuplas_vegetais)

print(f"Alimentos:{tuplas_final}")