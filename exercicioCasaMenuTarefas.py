from bibliotecaClasses import *
from arquivoDeDadosMenu import *

arq = "arquivoListasDoUsuario.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    respostaUsuario = menu(["INSERIR GANHOS","LISTAR GANHOS","DELETAR GANHOS","SAIR DO APLICATIVO"])
    if respostaUsuario == 1 :
        # OPÇAO DE INSERIR GANHOS
        cabecalho("NOVO GANHO!")
        app = str(input("UBER ou 99? : "))
        ganho = opçaoUsuario("Digite o Valor apurado: ")
        cadastrar(arq, app, ganho)
    elif respostaUsuario == 2:
        # OPÇÃO DE LISTAR ARQUIVO LISTAR GANHOS
        lerArquivo((arq))
    elif respostaUsuario == 3 :
        #OPÇAO DE DELETAR GANHOS
        deletar = opçaoUsuario("ESCOLHA UM ITEM PARA EXCLUIR")
        #print("DELETAR GANHOS")
    elif respostaUsuario == 4 :
        print("ENCERRANDO ATIVIDADES DO DIA. BOM DESCANSO! EXCELENTE TRABALHO!")
        break
    else:
        print("\033[31mERRO! DIGITE UMA OPÇAO VÁLIDA!\033[m")

