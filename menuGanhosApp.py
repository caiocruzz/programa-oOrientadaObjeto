from bibliotecaClasses import *
from arquivoDeDadosMenu import *

arq = "arquivoListasDoUsuario.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    respostaUsuario = menu(["INSERIR GANHOS","LISTAR GANHOS","DELETAR GANHOS","SAIR DO APLICATIVO"])
    if respostaUsuario == 1 :
        print("INSERIR GANHOS")
    elif respostaUsuario == 2:
        print("LISTAR GANHOS")
    elif respostaUsuario == 3 :
        print("DELETAR GANHOS")
    elif respostaUsuario == 4 :
        print("ENCERRANDO ATIVIDADES DO DIA. BOM DESCANSO! EXCELENTE TRABALHO!")
        break
    else:
        print("ERRO! DIGITE UMA OPÇAO VÁLIDA!")