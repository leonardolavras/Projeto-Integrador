def deletar():
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
    print('Deletar amostras'.center(75))
    print("-=" * 40)
    print('\n')

    consulta = 'SELECT ID, MP10, MP25, O3, CO, NO2, SO2 FROM AMOSTRAS'
    mycursor.execute(consulta)
    linhas = mycursor.fetchall()

    if len(linhas) == 0:
        print('Não há amostras disponíveis para exclusão.')
        return

    for linha in linhas:
        print('ID =', linha[0])
        print('MP10 =', linha[1])
        print('MP25 =', linha[2])
        print('O3 =', linha[3])
        print('CO =', linha[4])
        print('NO2 =', linha[5])
        print('SO2 =', linha[6])
        print('-' * 40)

    excluir = input('Qual o ID da amostra que deseja excluir: ')

    ids_disponiveis = [linha[0] for linha in linhas]

    if excluir not in ids_disponiveis:
        print("\n")
        print('ID incorreto. Por favor, digite um ID válido.')
        mycursor.close()
        return

    sql = 'DELETE FROM AMOSTRAS WHERE ID = %s'
    try:
        mycursor.execute(sql, (excluir,))
        mydb.commit()
        print('\n')
        print('Sucesso!! Registro excluído.')
    except:
        print('Não foi possível excluir esse registro')

    mycursor.close()
