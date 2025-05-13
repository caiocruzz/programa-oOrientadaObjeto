class Pessoa():
    def __init__(self, nome , idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=False
        self.dormindo=False
        self.falando=False

    def falar(self):
        if self.falando == True:
            print(f"{self.nome} está falando.")
        elif self.comendo == True:
            print(f"{self.nome} está comendo.")
        elif self.dormindo == True:
            print(f"{self.nome} está dormindo.")
        else:
            self.falando = False
            print(f"{self.nome} começou a falar")
    def comer(self):
        if self.comendo == True:
            print(f"{self.nome} está comendo.")
        elif self.falando == True:
            print(f"{self.nome} está falando.")
        elif self.dormindo == True:
            print(f"{self.nome} está dormindo.")
        else:
            self.comendo = False
            print(f"{self.nome} começou a comer.")

    def dormir(self):
        if self.dormindo == True:
            print(f"{self.nome} já está dormindo.")
        elif self.comendo == True:
            print(f"{self.nome} está comendo.")
        elif self.falando == True:
            print(f"{self.nome} está falando.")
        else:
            self.dormindo = False
            print(f"{self.nome} foi dormir.")

    def pararDeFalar(self):
        if self.falando == True :
            print(f"{self.nome} ja está falando.")
        else:
            self.falando = False

    def pararDeComer(self):
        if self.comendo == True:
            print(f"{self.nome} está comendo.")
        else:
            self.comendo = False

    def acordar(self):
        if self.dormindo == True:
            print(f"{self.nome} acordou ")
        else:
            self.dormindo = False
            print(f"{self.nome} Foi dormir.")


class ContaBancaria():
    def __init__(self, numeroDaConta, nomeCliente, tipoDeConta ):
        self.numeroDaConta=numeroDaConta
        self.saldoDaConta=0
        self.statusConta= False
        self.nomeCliente=nomeCliente
        self.tipoDeConta=tipoDeConta


    def verificarSaldo(self):
        if self.statusConta == True:
            print(f"Saldo da Conta:{self.saldoDaConta}")
        else:
            print(f"Conta inativa:")

    def saldoDaconta(self):
        if self.statusConta == True :
            print(f"Saldo da Conta:{self.saldoDaConta}")
        else:
            print(f"Conta Inativa.")

    def depositar(self,deposito):
        if self.statusConta == True:
            self.saldoDaConta = deposito + self.saldoDaConta
            print(f"Você fez um deposito de: R${deposito}")
        elif self.statusConta == False:
            print(f"Conta Inativa.")

    def sacar(self,saque):
        if self.statusConta == True :
           self.saldoDaConta = self.saldoDaConta - saque
           print(f"Você realizou um saque no valor de: R${saque} Seu Saldo Atual é de: R${self.saldoDaConta}")
        else:
            print(f"Conta Inativa!")

    def ativarConta(self):
        if self.statusConta == True :
            print(f"Sua conta está ativa.")
        else:
            self.statusConta = True
            print(f"Você ativou sua conta.")

    def desativarConta(self):
        if self.saldoDaConta >0:
            print(f"Você não pode desativar sua conta, pois seu saldo está positivo. {self.saldoDaConta}")
        elif self.statusConta == True and self.saldoDaConta == 0 :
            print(f"Você desativou sua conta.")


def formato( tam = 42):
    return "_" * tam

def cabecalho(txt):
    print(formato())
    print(txt.center(42))
    print(formato())

def menu(lista):
    cabecalho("GANHOS DO DIA APPMOTO ")
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(formato())
    opção = opçaoUsuario("ESCOLHA UMA OPÇAO: ")
    return opção

def opçaoUsuario(msg):
    while True:
        try:
            numeroUsuario = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um numero inteiro.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return numeroUsuario

# aula 13.05
class Animal():
    def __init__(self,nome, cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f"O {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f"O {self.nome} foi miando...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def latir(self):
        print(f"O {self.nome} foi latir. ")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def mugir(self):
        print(f"A Vaca {self.nome} foi mugir. ")

class Coelho(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome,cor)

    def guinchar(self):
        print(f"O Coelho {self.nome} tem olhos vermelhos e pelos {self.cor} ")


class Ingressos():
    def __init__(self,valor):
        self.valor=valor

    def imprimirValor(self):
        print(f"Seu ingresso custa: R$:{self.valor}")



class Vip(Ingressos):
    def __init__(self,valor):
        super().__init__(valor)
        self.valor*=1.5
    def imprimirValor(self):
        print(f"Seu ingresso VIP custou: {self.valor}")


class Forma():
    def __init__(self,area,perimetro):
        self.area=0
        self.perimetro=0



class Retangulo(Forma):
        def __init__(self):
            super().__init__(self)

        def calculaArea(self,base,altura):
            self.area = base * altura
            print(f"A area do retangulo é:{self.area}")
        def calculaPerimetro(self,base, altura):
            self.perimetro=2*(base+altura)
            print(f"O perimetro do Retangulo é {self.perimetro}")


class Triangulo(Forma):
        def __init__(self):
            super().__init__(self)

        def calculaArea(self,base,altura):
            self.base=base
            self.altura=altura
            self.area = self.base * self.altura
            print(f"A area do retangulo é:{self.area}")
        def calculaPerimetro(self, base, altura):
            self.perimetro = 2 * (base + altura)
            print(f"O perimetro do Triangulo é: {self.perimetro}")



class Atleta():
    def __init__(self):
        self.aposentado=False
        self.peso=0
        self.aquecido=False

    def aposentar(self):
        self.aposentado=True
        print(f"Aposentado")
    def aquecer(self):
        self.aquecido=True
        print(f"Aquecido")

class Corredor(Atleta):
    def __init__(self):
        super().__init__()

    def correr(self):

        print(f"Foi correr!")

class Nadador(Atleta):
    def __init__(self):
        super().__init__()

    def nadar(self):
        print(f"Foi nadar!")

class Ciclista(Atleta):
    def __init__(self):
        super().__init__()

    def pedalar(self):
        print(f"Foi pedalar")

class Triatleta(Corredor,Nadador,Ciclista):
    def __init__(self):
        super().__init__()





