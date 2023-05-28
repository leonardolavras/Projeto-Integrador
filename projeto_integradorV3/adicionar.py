
def adicionar():
    import mysql.connector
    mydb = mysql.connector.connect(
    host="us-cdbr-east-06.cleardb.net",
    user="b5390412538351",

    password="e827f4fc",
    database="heroku_a8dd37572b9035f"
    )
    mycursor = mydb.cursor()
    print('\n')
    print("-="*40)
    print('inserir'.center(60))
    print("-="*40)
    print('\n')
    while True:
        try:
            MP10= int(input('Digite a quantidade de particulas inalaveis: '))
            MP25 = int(input('Digite a quantidade de particulas inalaveis finas: '))
            O3 = int(input('Digite a quantidade de ozonio: '))
            CO = int(input('Digite a quantidade de monoxio de carbono: '))
            NO2 = int(input('Digite a quantidade de dioxido de nitrogenio: '))
            SO2 = int(input('Digite a quantidade de dioxido de enxofre: '))
        except:
            print('Digite valores numericos! Tente novamente')
        else:
            if MP10 <0 or MP25 <0 or O3 <0 or CO<0 or NO2<0 or SO2<0:
                print('São aceitos apenas valores positivos')
            else:

                ParInaS = str(MP10)
                ParInaFS = str(MP25)
                OzonioS = str(O3)
                MonoCarbS = str(CO)
                DioNitroS = str(NO2)
                DioEnxS = str(SO2)


                dados = ParInaS + ',' + ParInaFS + ',' + OzonioS + ',' +MonoCarbS+ ','+DioNitroS+','+DioEnxS+')'
                declaracao = """INSERT INTO heroku_a8dd37572b9035f.amostras
                (ID, MP10, MP25,O3,CO,NO2,SO2)
                VALUES (default,"""
                sql = declaracao + dados
                
                print('\n')
                try:
                    mycursor.execute(sql)
                    mydb.commit()
                    mycursor.close()
                except:
                    print('Erro ao inserir no banco de dados')
                else:
                    print('Inserido com sucesso')
                return






