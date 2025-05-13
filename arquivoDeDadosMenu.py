from idlelib.query import Query

from bibliotecaClasses import *

def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome,"wt+")
        a.close()
    except:
        print("ERRO NA CRIAÇÃO DO ARQUIVO!")
    else:
        print(f"Arquivo {nome} criado com Sucesso!")

def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("ERRO AO LER ARQUIVO!")
    else:
        cabecalho("GANHOS POR APP")
        for linha in a :
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", " ")
            print(f"{dado[0]:<30} R$:{dado[1]:>3}")
    finally:
        a.close()

def cadastrar(arq, app="uber ou 99", ganho=0):
    try:
        a = open(arq, "at")
    except:
        print("ERRO AO ABRIR O ARQUIVO")
    else:
        try:
            a.write(f"{app};{ganho}\n")
        except:
            print("HOUVE UM ERRO NA HORA DE INSERIR OS DADOS!")
        else:
            print(f"VOCÊ FEZ {ganho} RODANDO NA PLATAFORMA {app} HOJE")
            a.close()

def deletar(arq, app="", ganho=0):
    try:
        a = open(arq, "at")
    except:
        print("ERRO AO ABRIR O ARQUIVO")
    else:
        try:
            a.write(f"{app};{ganho}\n")
        except:
            print("HOUVE UM ERRO NA HORA DE INSERIR OS DADOS!")
        else:
            print(f"VOCÊ FEZ {ganho} RODANDO NA PLATAFORMA {app} HOJE")
            a.close()