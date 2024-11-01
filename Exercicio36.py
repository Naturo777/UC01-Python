import random   
def Game(numero):
    player2=random.randint(0,5)
    
    if (numero+player2)%2==0:
        return "PAR - Player1 venceu!"
    else:
        return "ÍMPAR - Player2 venceu!"
print("Jogo - Par ou Ímpar")
print("Números permitidos - 0,1,2,3,4 ou 5")
print()
print("-----------------------")
print()
player1=int(input("Insira a sua jogada: "))
print(f'{Game(player1)}')
