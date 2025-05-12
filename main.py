lista_tarefas = ["Varrer a casa", "Arrumar a cama", "Lavar a louça"]

opc1 = 0
removeu_item = False
while opc1 != 4:
    opc1 = int(input("O que deseja fazer:\n1-Adicionar itens na lista\n2-Remover um item da lista\n3-Ver os itens da lista\n4-Sair do programa:\n"))
    if opc1 == 1:
        opc2 = "s"
        adicionar = "Nada"
        indice_add = 0
        while opc2 == "s" or opc2 == "S":
            adicionar = input("Digite o que deseja adicionar na lista: ")
            lista_tarefas.append(adicionar)
            indice_add +=1
            opc2 = input("Deseja adicionar mais um item na lista(S/N)? ")
        
    elif opc1 == 2:
        opc3 = "s"
        indice_pop = 0
        lista_removidos = []
        removeu_item = True
        while opc3 == "s" or opc3 == "S":
            indice_pop = int(input("Digite o indice que deseja remover da lista: "))
            removido = lista_tarefas.pop(indice_pop)
            lista_removidos.append(removido)
            indice_pop +=1
            opc3 = input("Deseja remover mais um item na lista(S/N)? ")
    
    elif opc1 == 3:
        print("\nItens na lista: ", end="")
        for i in range(len(lista_tarefas)):
            print(lista_tarefas[i], end=", ")
        print("\n")
        
        if removeu_item == True:
            print("\nItens removidos")
            for j in range(len(lista_removidos)):
                print(lista_removidos[j], end=", ")
            print("\n\n")
            
    elif opc1 == 4:
        break
    
    else:
        print("Favor, digite um valor valido!")
        opc1 = int(input("O que deseja fazer: 1-Adicionar itens na lista\n2-Remover um item da lista\n3-Ver os itens da lista\n4-Sair do programa"))
        
print("programa encerrado!")