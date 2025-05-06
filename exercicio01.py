from bibliotecaClasses import Pessoa

aluno01 = Pessoa("tchetche",32,90)
#aluno02 = Pessoa("Roben",34,97)
print(f"{aluno01.nome} tem {aluno01.idade} anos e pesa {aluno01.peso} quilos.")
#print(f"{aluno02.nome} tem {aluno02.idade} anos e pesa {aluno02.peso} quilos.")
aluno01.falar()
aluno01.comer("limao")
aluno01.dormir()