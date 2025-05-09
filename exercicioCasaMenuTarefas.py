menu = [1,2,3,4]
inserirTarefas = 2
listarTarefas = 1
deletarTarefas = 3
sair = 4
tarefas = ["ACORDAR", "CURSO" , "TRABALHAR"]
listaTarefaExcluida = []
esc = False

while True :
    print(menu)
    opcao = input("Digite um numero para escolher a opçao do Menu: ")

    for opcao in menu :
        if opcao == listarTarefas:
            print(tarefas)

        elif opcao == inserirTarefas:
            novaTarefa = input("Insira uma nova Tarefa: ")
            tarefas.append(novaTarefa)
            print(tarefas)

        if opcao == deletarTarefas :
            excluirTarefas = tarefas.pop()
            print(tarefas)
            print(f"Tarefa excluída: {excluirTarefas}")
            listaTarefaExcluida.append(excluirTarefas)


        if opcao not in menu :
            print("Opçao Invalida!")

        esc = True
        if opcao == sair or esc:
            esc = False
    break