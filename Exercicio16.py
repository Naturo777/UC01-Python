# Opção 1
a= int (input("Digite o primeiro número: "))
b= int (input("Digite o segundo número: "))
c= int (input("Digite o terceiro número: "))
if(a>b):
    if(a>c):
        print( "O primeiro número é o maior!")
    elif(c>b):
        print ( "O terceiro número é o maior!")
    elif (b>c):
        print ("O segundo número é o maior!")  

        #Opção 2

a= int (input("Digite o primeiro número: "))
b= int (input("Digite o segundo número: "))
c= int (input("Digite o terceiro número: "))
if(a>b and a>c):
        print( "O primeiro número é o maior!")
elif(b>a and b>c):
        print ("O segundo número é o maior!")
else: print("O terceiro é maior!")
     
     #Opção 3 
a= int (input("Digite o primeiro número: "))
b= int (input("Digite o segundo número: "))
c= int (input("Digite o terceiro número: "))
if (a==b and a==c):
    print ("Os 3 valores são iguais")
elif(a>b and a>c)
if(a>b and a>c):
        print( "O primeiro número é o maior!")
elif(b>a and b>c):
        print ("O segundo número é o maior!")
else: print("O terceiro é maior!")

#Opção 4 
a= int (input("Digite o primeiro número: "))
b= int (input("Digite o segundo número: "))
c= int (input("Digite o terceiro número: "))
valores=[a,b,c]
valores.sort()
valores.reverse()
print(valores[0])