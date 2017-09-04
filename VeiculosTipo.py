 # -*- coding: utf-8 -*-
from VeiculosAbstratos import Veiculo

'''
Descrição: Classe que guarda os objetos do tipo Carro e é uma classe derivada da Super Classe Veiculo (Classe abstrata) 

Utilização: funciona para diferenciar os tipos de veículos de acordo com suas peculiaridades

Parâmetros:
	Ela recebe todos os parâmetros que veículo recebe, mais a quantidade de portas que possui, podendo ser 2 ou 4.
'''
class Carro(Veiculo):
	def __init__(self, fabricante, modelo, quantidadePortas, autonomia, ano, placa, renavam, chassi, reservado = False):
		Veiculo.__init__(self, fabricante, modelo, autonomia, ano, placa, renavam, chassi, reservado = False)
		self.__quantidadePortas = __validaQuantPortas(quantidadePortas)

	# Descrição: O método realiza a validação da quantidade de portas, analisando se possui 2 ou 4, se não aciona um erro
	def __validaQuantPortas(self, quantidadePortas):
		if int(quantidadePortas) != 2 or int(quantidadePortas) != 4:
			raise ValidationError("Quantidade inválida, o carro deve possuir 2 ou 4 portas")
		return int(quantidadePortas)



'''
Descrição: Classe que guarda os objetos do tipo Van e é uma classe derivada da Super Classe Veiculo (Classe abstrata) 

Utilização: funciona para diferenciar os tipos de veículos de acordo com suas peculiaridades

Parâmetros:
	Ela recebe todos os parâmetros que veículo recebe, mais a capacidade de pessoas.
'''
class Van(Veiculo):
	def __init__(self, fabricante, modelo, capacidadePessoas, autonomia, ano, placa, renavam, chassi, reservado = False):
		Veiculo.__init__(self, fabricante, modelo, autonomia, ano, placa, renavam, chassi, reservado = False)
		self.__capacidadePessoas = __validaCapacidadePessoas(capacidadePessoas)

		#Descrição: realiza a validação da capacidade de pessoas, analisando se é um número
		def __validaCapacidadePessoas(self, capacidade):
			if capacidade.isdigit():
				return int(capacidade)
			raise ValidationError("A capacidade de pessoas deve ser um número")



'''
Descrição: Classe que guarda os objetos do tipo Utilitario e é uma classe derivada da 
		   Super Classe Veiculo (Classe abstrata) 

Utilização: funciona para diferenciar os tipos de veículos de acordo com suas peculiaridades

Parâmetros:
	Ela recebe todos os parâmetros que veículo recebe, mais a capacidade da Caçamba
'''
class Utilitarios(Veiculo):
	def __init__(self, fabricante, modelo, capacidadeCacamba, autonomia, ano, placa, renavam, chassi, reservado = False):
		Veiculo.__init__(self, fabricante, modelo, autonomia, ano, placa, renavam, chassi, reservado = False)
		self.__capacidadeCacamba = capacidadeCacamba

		#Descrição: realiza a validação da capacidade da Caçamba, analisando se é um número
		def __validaCapacidadeCacamba(self, capacidade):
			if capacidade.isdigit():
				return int(capacidade)
			raise ValidationError("Capacidade da camçamba deve ser um número")
		
		