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

# Conta quantos números são maiores que 10
count_maior_que_10 = sum(1 for num in numeros if num > 10)

# Exibe o resultado
print(f"\nQuantidade de números maiores que 10: {count_maior_que_10}")