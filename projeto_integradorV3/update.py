def update():
    import mysql.connector
    
    mydb = mysql.connector.connect(
        host="us-cdbr-east-06.cleardb.net",
        user="b5390412538351",
        password="e827f4fc",
        database="heroku_a8dd37572b9035f"
    )
    
    mycursor = mydb.cursor()
    print('\n')
    print("-=" * 40)
    print('Alterar amostras'.center(60))
    print("-=" * 40)
    print('\n')
    
    consulta = 'SELECT ID, MP10, MP25, O3, CO, NO2, SO2 FROM AMOSTRAS'
    mycursor.execute(consulta)
    linhas = mycursor.fetchall()

    
    
    if len(linhas) == 0:
        print('Não há amostras disponíveis para alterar.')
        return

    print('Amostras disponíveis para alteração:')
    for linha in linhas:
        print('ID:', linha[0])
        print('MP10:', linha[1])
        print('MP25:', linha[2])
        print('O3:', linha[3])
        print('CO:', linha[4])
        print('NO2:', linha[5])
        print('SO2:', linha[6])
        print('-' * 40)

    tipo = input('Digite o ID da amostra que você deseja alterar: ')
    if not tipo.isdigit():
        print('ID inválido. Digite um valor numérico válido.')
    


    sql = f"SELECT * FROM AMOSTRAS WHERE ID = {tipo}"
    mycursor.execute(sql)
    result = mycursor.fetchone()

    if result is None:
        print('ID não encontrado. Digite um ID válido.')
    
   
    
    while True:
        muda = int(input('Qual desses campos deseja alterar?: '))
        if muda >= 1 and muda <= 6:
            break
        else:
            print('Digite valores entre 1 e 6')
            print('Tente novamente!!')
    
    campos = ['MP10', 'MP25', 'O3', 'CO', 'NO2', 'SO2']
    muda = campos[muda - 1]

    consulta = f'SELECT {muda} FROM AMOSTRAS WHERE ID = {tipo}'
    mycursor.execute(consulta)
    linhas = mycursor.fetchall()
    muda2 = str(linhas[0][0])

    novo = input('Digite o novo valor: ')
    sql = f"UPDATE AMOSTRAS SET {muda} = '{novo}' WHERE ID = {tipo}"
    try:
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        print('\n')
        print('Amostra alterada!')
    except:
        print('Não foi possível alterar a amostra')
    
        return
    else:
        print('\n')
        print('Erro ao alterar amostra!')
    return

update()