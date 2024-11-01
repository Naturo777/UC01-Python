# Cria uma lista vazia para armazenar os números
numeros = []

# Coleta cinco números do usuário
for i in range(5):
    while True:
        try:
            numero = float(input(f"Digite o {i + 1}º número: "))
            numeros.append(numero)  # Adiciona o número à lista
            break  # Sai do loop se a entrada for válida
        except ValueError:
            print("Por favor, insira um número válido.")

# Ordena a lista em ordem crescente
numeros.sort()

# Exibe os números em ordem crescente
print("\nNúmeros em ordem crescente:")
print(numeros)