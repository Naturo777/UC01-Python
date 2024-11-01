# Criando uma lista para armazenar as informações dos alunos
alunos = []

# Coletando informações de 5 alunos
for i in range(5):
    print(f"\nAluno {i + 1}:")
    nome = input("Digite o nome: ")
    
    while True:
        try:
            media = float(input("Digite a média (entre 0 e 10): "))
            if 0 <= media <= 10:
                alunos.append({'nome': nome, 'media': media})
                break  # Saindo do loop se a média é válida
            else:
                print("A média deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

# Exibindo as informações dos alunos
print("\nAlunos e suas médias:")
for aluno in alunos:
    print(f"Nome: {aluno['nome']}, Média: {aluno['media']:.2f}")