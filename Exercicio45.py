alunos=[]
medias=[]
def preencheListas():
    for i in range (10):
        alunos.append(input(f"Digite o nome do {i+1}º: "))
        medias.append(float(input(f"Digite o nome do {i+1}º aluno: ")))
        return
def retornaMaiores():
    for i in range(10):
        if(medias[i]>=6):
            print(f'aluno{alunos[i]} com média {medias[i]}')
preencheListas()
retornaMaiores()