# crie uuma conta bancaria
from bibliotecaClasses import ContaBancaria

Cliente01 = ContaBancaria(1, "jeremias", "corrente")
Cliente02= ContaBancaria(2,"jose","corrente")
Cliente02.saldoDaconta()
Cliente02.ativarConta()
Cliente02.verificarSaldo()
Cliente02.depositar(10)
Cliente02.depositar(10)
Cliente02.verificarSaldo()
Cliente02.sacar(5)
Cliente02.desativarConta()
Cliente02.sacar(15)
Cliente02.desativarConta()