# Criando uma lista para armazenar as informações das pessoas
pessoas = []

# Coletando informações de 10 pessoas
for i in range(10):
    print(f"\nPessoa {i + 1}:")
    nome = input("Digite o nome: ")
    bairro = input("Digite o bairro: ")
    pessoas.append({'nome': nome, 'bairro': bairro})

# Ordenando a lista de pessoas por nome
pessoas_ordenadas = sorted(pessoas, key=lambda x: x['nome'])

# Exibindo os nomes e bairros em ordem alfabética
print("\nPessoas em ordem alfabética:")
for pessoa in pessoas_ordenadas:
    print(f"Nome: {pessoa['nome']}, Bairro: {pessoa['bairro']}")