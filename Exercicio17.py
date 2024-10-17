print(f"Vamos calcular o seu IMC! " )

Peso=float (input("Digite o seu peso: "))
Altura=float (input("Digite a sua altura: "))
IMC=(Peso/Altura*Altura)
print(f"IMC: {IMC} ")
if(IMC>25):
    print ("Peso acima do ideal!")
else:
    print ("Peso OK!")