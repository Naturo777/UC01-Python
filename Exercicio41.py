# Cria uma lista vazia para armazenar os números
numeros = []

# Coleta oito números do usuário
for i in range(8):
    while True:
        try:
            numero = float(input(f"Digite o {i + 1}º número: "))
            numeros.append(numero)  # Adiciona o número à lista
            break  # Sai do loop se a entrada for válida
        except ValueError:
            print("Por favor, insira um número válido.")

# Determina o maior e o menor número
maior = max(numeros)
menor = min(numeros)

# Exibe os resultados
print(f"\nO maior número é: {maior}")
print(f"O menor número é: {menor}")