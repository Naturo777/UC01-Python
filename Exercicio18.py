nota1=float (input("Digite a primeira nota: "))
nota2=float (input("Digite a segunda nota: "))
media=(nota1+nota2)/2
print(f"A média do aluno é: {media} ")
if(media<4):
    print ("aluno reprovado direto")
elif(media>7):
    print ("aluno aprovado direto")
else:
    print("Aluno em recuperação")    
    
    rec=float (input("Digite a sua nota de recuperação: "))
    if(rec<5):
        print("Reprovado na recuperação")

    else:
        print ("aluno aprovado na recuperação")
