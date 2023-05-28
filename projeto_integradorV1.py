print("Esse programa ele qualificara a qualidade do ar de acordo com os dados inseridos pelo usuário!!!\n")


while True: 
    try:
        mp10 = float(input("Digite o valor das particulas inaláveis: "))
        mp25=float(input("Digite o valor das particulas finas: "))
        o3= float(input("Digiite o valor do ozonio: "))
        co=float(input("Digite o valor do monoxido de carbono: "))
        no2=float(input("Digite o valor do dioxido de nitrogenio: "))
        so2=float(input("Digite o valor do dioxido de enxofre: "))
        
        if mp10 < 51 and mp25 < 26 and o3 < 101 and co < 10 and no2 < 201 and so2 < 21:
         qualidade = "BOA.\n" 
         print("A qualidade do ar é", qualidade, "não há efeito a saúde.\n")
         
        elif mp10 <= 100 and mp25 <=50 and o3 <=130 and co <=11 and no2 <=240 and so2 <=40:
          qualidade = "MODERADA.\n"
          print("A qualidade do ar é", qualidade,"\n",)
          print("Os efeitos na saúde são:\n")
          print("Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratônias e cardiacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.\n")
        
        elif mp10 <= 150 and mp25 <=75 and o3 <=160 and co <=13 and no2 <=320 and so2 <=365:
          qualidade = "RUIM.\n"
          print("A qualidade do ar é,", qualidade,"\n",) 
          print("Os efeitos na saúde são:\n")
          print("Toda a população pode apresentar sintomas como fosse seca, cansaço,ardor nos olhos, nariz e garganta, Pessoas de grupos sensiveis (crianças, idosos e pessoas com doenças respiratórias e cardiacas) podem apresentar efeitos mais sérios na saude\n")
        
        
        elif mp10 <= 250 and mp25 <=125 and o3 <=200 and co <=15 and no2 <=1130 and so2 <=800:
           qualidade = "MUITO RUIM."
           print("A qualidade do ar é", qualidade,"\n",)
           print("Os efeitos na saúde são:")
           print("Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardiacas).\n")
        
        elif mp10 > 250 or mp25 > 125 or o3 > 200 or co > 15 or no2 > 1130 or so2 > 800:
           qualidade = "PÉSSIMA."
           print("A qualidade do ar é", qualidade,"\n",)
           print("Os efeitos na saúde são:")
           print("Toda a população pode apresentar sérios riscos de manfestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensiveis.\n")
           
    except:
      print("Os dados tem que ser numéricos, tente novamente!!\n")
   
     
    while True: 
        respostas = input ("Deseja continuar classificando a qualidade do ar (S/N)? ").upper()
        if respostas not in ["S", "N"]:
            print("É preciso digitar S ou N!")
        
        else:
           break
    if respostas in ["n","N"]:
        break
print("Obrigado por usar esse programa!")