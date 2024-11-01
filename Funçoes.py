def media (n1,n2,n3,n4 ):
    media=( n1+n2+n3+n4)/4
    if(media>=7):
        return "Aprovado"
    elif(media<7 and media>4):
        return "RECUPERAÇÃO"
    else:
        return "RECUPERAÇÃO"

def DefineMedia(nome):
    notas=[]
    for i in range(4):
        notas.append(float(input(f"Digite a {i+1}ª nota: ")))
print (f'O aluno {nome} está: {Media(notas[0],notas[1],notas[2],notas[3],notas[4])}')

for i in range(5):
    nomeAluno=input("Digite o nome do aluno: ")
    DefineMedia(nomeAluno)