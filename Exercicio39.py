# Cria uma lista vazia para armazenar os números
numeros = []

# Coleta seis números do usuário
for i in range(6):
    while True:
        try:
            numero = float(input(f"Digite o {i + 1}º número: "))
            numeros.append(numero)  # Adiciona o número à lista
            break  # Sai do loop se a entrada for válida
        except ValueError:
            print("Por favor, insira um número válido.")

# Exibe os números na ordem digitada
print("\nNúmeros digitados na ordem:")
for numero in numeros:
    print(numero)