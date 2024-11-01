# Função para exibir a mensagem personalizada
def mensagem_bem_vindo(nome, cidade):
    if cidade.lower() == "rio de janeiro":
        return f"Seja bem-vindo à Cidade Maravilhosa, {nome}!"
    else:
        return f"{nome}, você mora em {cidade}."

# Solicita ao usuário que digite seu nome e sua cidade
usuario_nome = input("Digite seu nome: ")
usuario_cidade = input("Digite sua cidade: ")

# Chama a função e armazena a mensagem
resultado = mensagem_bem_vindo(usuario_nome, usuario_cidade)

# Exibe a mensagem
print(resultado)