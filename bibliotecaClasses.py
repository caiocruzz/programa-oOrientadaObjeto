class Pessoa():
    def __init__(self, nome , idade, peso, falando):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=False
        self.dormindo=False
        self.falando=False
    def falar(self):
        print(f"{self.nome} começou a falar")
    def comer(self, comida):
        if self.comendo == True:
            print()
   # print(f"Foi comer {comida} ")
    def dormir(self, sono):
        print(f"dorme nunca {sono}")
    