# Cria uma lista vazia para armazenar os números
numeros = []

# Coleta dez números do usuário
for i in range(10):
    while True:
        try:
            numero = float(input(f"Digite o {i + 1}º número: "))
            numeros.append(numero)  # Adiciona o número à lista
            break  # Sai do loop se a entrada for válida
        except ValueError:
            print("Por favor, insira um número válido.")

# Calcula a soma e a média
soma = sum(numeros)
media = soma / len(numeros)

# Exibe os resultados
print(f"\nSoma: {soma}")
print(f"Média: {media:.2f}")