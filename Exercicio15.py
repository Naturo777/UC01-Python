# Solicita ao usuário que digite três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifica qual número é o maior
maior = num1  # Assume que o primeiro número é o maior inicialmente

if num2 > maior:
    maior = num2  # Atualiza maior se o segundo número for maior
if num3 > maior:
    maior = num3  # Atualiza maior se o terceiro número for maior

# Exibe o maior número
print(f"O maior número entre {num1}, {num2} e {num3} é: {maior}")