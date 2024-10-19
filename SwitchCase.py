#value = 3 

#match value:

    #Case 1:    
        #result: "one"
    #Case 2:
        #result:"two"    
    #Case 3:
        #result:"three"
    #Case _: 
        #result: "default"

#print (result)

total=0
escolha=0
while(escolha!=5):
    print ( "Cardápio:")
    print (" 1 - calabresa com cebola - R$25,00 \n 2- camarão com catupiry - R$26,00\n 3- frango com requeijão - R$27,00\n 4- banana com chocolate R$28,00" )
    print( "5- Finalizar pedido")
    escolha = int (input("Digite a sua opção escolhida: "))
    match escolha:
        case 1:
            print("1 - calabresa com cebola - 25,00")
            total+=25.0
        case 2:
            print("2- camarão com catupiry - 26,00")
            total+=26.0
        case 3: 
            print:("3- frango com requeijão - 27,00")
            total+=27.0
        case 4: 
            print:("4- banana com chocolate - 28,00")
            total+=28.0
        case 5:
            print(f'Total do pedido:R${total}')
        
        case _:
            print ("Escolha uma opção válida: ")