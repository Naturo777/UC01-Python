player1=input("Escolha sua opção: Pedra, Papel ou tesoura: ")
player2=input("Escolha sua opção: Pedra, Papel ou tesoura: ")
if(player1==player2):
    print("Empate")
elif((player1=="pedra" and player2=="tesoura") or (player1=="papel" and player2== "pedra" ) or (player1=="tesoura" and player2=="papel")):
    print("Player1 venceu!!! ({player1} vence de {player2})")
else:
    print("Player2 venceu!!! ({player2} vence de {player1})")             