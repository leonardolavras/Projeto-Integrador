
import classificar 
import adicionar 
import deletar
import update 

def Menu():
    while True:

        
        print('\n')
        print("-="*40)
        print('Menu Principal'.center(75))
        print("-="*40)
        print('\n')
        print("Escolha o numero de acordo com a ação que deseja fazer!".center(65))
        print('\n')
        print("1- Incluir amostra")
        print("2- Alterar amostra")
        print("3- Excluir amostra")
        print("4- Classificar o ar")
        print("5- Sair do Sistema\n")
        
        
        pick=input("Escolha a opção que deseja: ")
        print("="*217)
        print("\n")
        
        
        if pick == "1":
            adicionar.adicionar()
        
        elif pick =="2":
            update.update()           
        
        elif pick =="3":
            deletar.deletar()           
        
        elif pick =="4":
            classificar.classificar()
        
        elif pick =="5":
            print("Obrigado por usar este programa!")
            break
        else:
            print('Digite um valor válido!')

Menu() 