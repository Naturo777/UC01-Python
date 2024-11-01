# Função para verificar se um número é par ou ímpar
def verificar_paridade(nota):
    if nota % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Lista para armazenar as notas
notas = []

# Coletando quatro notas
for i in range(4):
    while True:
        try:
            nota = float(input(f"Digite a nota {i + 1}: "))
            notas.append(nota)
            break  # Sai do loop se a nota for válida
        except ValueError:
            print("Por favor, insira um número válido.")

# Verificando e exibindo se cada nota é par ou ímpar
print("\nResultados:")
for nota in notas:
    paridade = verificar_paridade(nota)
    print(f"Nota {nota}: {paridade}")