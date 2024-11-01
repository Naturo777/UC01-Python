# Função para calcular a soma de dois números
def calcular_soma(num1, num2):
    return num1 + num2

# Solicita ao usuário que digite dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Chama a função e armazena o resultado
resultado = calcular_soma(numero1, numero2)

# Exibe o resultado da soma
print(f"A soma de {numero1} e {numero2} é: {resultado}")