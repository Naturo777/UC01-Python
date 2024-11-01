# Função para exibir a mensagem de boas-vindas
def boas_vindas(nome):
    print(f"Seja bem-vindo(a), {nome}!")

# Solicita ao usuário que digite seu nome
usuario_nome = input("Digite seu nome: ")

# Chama a função para exibir a mensagem
boas_vindas(usuario_nome)