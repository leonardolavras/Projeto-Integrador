
def classificar():
    import mysql.connector
    mydb = mysql.connector.connect(
    host="us-cdbr-east-06.cleardb.net",
    user="b5390412538351",

    password="e827f4fc",
    database="heroku_a8dd37572b9035f"
    )
    cursor = mydb.cursor()
    print("Classifque a qualidade do ar: ")
    consulta = 'select avg(MP10) from AMOSTRAS'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        MP10 = float(linha[0])

    consulta = 'select avg(MP25) from AMOSTRAS'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        MP25 = float(linha[0])

    consulta = 'select avg(O3) from AMOSTRAS'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        O3 = float(linha[0])

    consulta = 'select avg(CO) from AMOSTRAS'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        CO = float(linha[0])

    consulta = 'select avg(NO2) from AMOSTRAS'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        NO2 = float(linha[0])

    consulta = 'select avg(SO2) from AMOSTRAS'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        SO2 = float(linha[0])

            
        
    if MP10 < 51 and MP25 < 26 and O3 < 101 and CO < 10 and NO2 < 201 and   SO2 < 21:
        qualidade = "BOA.\n" 
        print("A qualidade do ar é", qualidade, "não há efeito a saúde.\n")
    
    elif MP10 <= 100 and MP25 <=50 and O3 <=130 and CO <=11 and NO2 <=240 and SO2 <=40:
        qualidade = "MODERADA.\n"
        print("A qualidade do ar é", qualidade,"\n",)
        print("Os efeitos na saúde são:\n")
        print("Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratônias e cardiacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.\n")
        
    elif MP10 <= 150 and MP25 <=75 and O3 <=160 and CO <=13 and NO2 <=320 and SO2 <=365:
        qualidade = "RUIM.\n"
        print("A qualidade do ar é,", qualidade,"\n",) 
        print("Os efeitos na saúde são:\n")
        print("Toda a população pode apresentar sintomas como fosse seca, cansaço,ardor nos olhos, nariz e garganta, Pessoas de grupos sensiveis (crianças, idosos e pessoas com doenças respiratórias e cardiacas) podem apresentar efeitos mais sérios na saude\n")
        
    
    elif MP10 <= 250 and MP25 <=125 and O3 <=200 and CO <=15 and NO2 <=1130 and SO2 <=800:
        qualidade = "MUITO RUIM."
        print("A qualidade do ar é", qualidade,"\n",)
        print("Os efeitos na saúde são:")
        print("Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardiacas).\n")
    
    elif MP10 > 250 or MP25 > 125 or O3 > 200 or CO > 15 or NO2 > 1130 or SO2 > 800:
        qualidade = "PÉSSIMA."
        print("A qualidade do ar é", qualidade,"\n",)
        print("Os efeitos na saúde são:")
        print("Toda a população pode apresentar sérios riscos de manfestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensiveis.\n")
        
    

    
    while True:
                
        respostas = input ("Deseja continuar classificando a qualidade do ar (S/N)? ").upper()
        if respostas not in ["S", "N"]:
            print("É preciso digitar S ou N!")

        elif respostas in ["s","S"]:
                classificar()

        else:
            
            if respostas in ["n","N"]:
                
                print("Obrigado por usar esse programa!")
            break

