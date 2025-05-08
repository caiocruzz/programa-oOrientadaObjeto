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
            self.falando == False

    def pararDeComer(self):
        if self.comendo() == True:
            print(f"{self.nome} está comendo.")
        else:
            self.comendo() == False

    def acordar(self):
        if self.dormindo() == True:
            self.dormindo() == False
            print(f"{self.nome} acordou ")
        else:
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
        elif self.statusConta == False:
            print(f"Conta Inativa.")

    def depositar(self,deposito):
        if self.statusConta == True:
            self.saldoDaconta = deposito + self.saldoDaConta
            print(f"{self.saldoDaconta}")
        elif self.statusConta == False:
            print(f"Conta Inativa.")

    def sacar(self,valor):
        if self.statusConta == True :
           self.saldoDaConta = self.saldoDaConta - valor
        else:
            print(f"Conta Inativa!")

    def ativarConta(self):
        if self.statusConta == True :
            print(f"Sua conta está ativa. {self.saldoDaConta}")
        else:
            self.statusConta = True
            print(f"Você ativou sua conta. {self.saldoDaConta}")