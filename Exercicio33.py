def ProgramasInfantis():
    lista1= ["Peppa Pig", "Chaves", "Pantera cor de Rosa", "Tom & Jerry"]
    print(lista1)
    return
def Carros():
    lista2=["Jeep Renegade - R$120.000", "Amarok -  R$350.000", "HB20 - R$230.000"]
    print(lista2)
    return

idade=int(input("Digite a sua idade:"))
if (idade>18):
        Carros()
else:
        ProgramasInfantis()