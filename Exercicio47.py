# Criando uma lista para armazenar as informações das pessoas
pessoas = []

# Coletando informações de 10 pessoas
for i in range(10):
    print(f"\nPessoa {i + 1}:")
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    cidade = input("Digite a cidade: ")
    pessoas.append({'nome': nome, 'telefone': telefone, 'cidade': cidade})

# Filtrando e exibindo as pessoas que moram em Campo Grande
print("\nPessoas que moram em Campo Grande:")
for pessoa in pessoas:
    if pessoa['cidade'].strip().lower() == 'campo grande':
        print(f"Nome: {pessoa['nome']}, Telefone: {pessoa['telefone']}")