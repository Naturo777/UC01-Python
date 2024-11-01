# Coleta sete números do usuário
for i in range(7):
    while True:
        try:
            numero = int(input(f"Digite o {i + 1}º número: "))  # Usa int para receber números inteiros
            if numero % 2 == 0:
                contagem_pares += 1  # Incrementa contador de pares
            else:
                contagem_impares += 1  # Incrementa contador de ímpares
            break  # Sai do loop se a entrada for válida
        except ValueError:
            print("Por favor, insira um número válido.")

# Exibe os resultados
print(f"\nQuantidade de números pares: {contagem_pares}")
print(f"Quantidade de números ímpares: {contagem_impares}")