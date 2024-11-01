# Função para calcular a média e verificar a aprovação
def verificar_aprovacao(notas):
    media = sum(notas) / len(notas)
    if media < 6:
        return f"Média: {media:.2f} - Aluno reprovado"
    else:
        return f"Média: {media:.2f} - Aluno aprovado"

# Lista para armazenar as notas
notas = []

# Coletando quatro notas
for i in range(4):
    while True:
        try:
            nota = float(input(f"Digite a nota {i + 1}: "))
            if 0 <= nota <= 10:  # Verifica se a nota está entre 0 e 10
                notas.append(nota)
                break  # Sai do loop se a nota for válida
            else:
                print("A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

# Verificando a aprovação
resultado = verificar_aprovacao(notas)
print("\n" + resultado)