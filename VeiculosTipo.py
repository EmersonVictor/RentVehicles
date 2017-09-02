 # -*- coding: utf-8 -*-
from VeiculosAbstratos import Veiculo

'''
Descrição: Classe que guarda os objetos do tipo Carro e é uma classe derivada da Super Classe Veiculo (Classe abstrata) 

Utilização: funciona para diferenciar os tipos de veículos de acordo com suas peculiaridades

Parâmetros:
	Ela recebe todos os parâmetros que veículo recebe, mais a quantidade de portas que possui, que pode ser 2 ou 4.

'''
class Carro(Veiculo):
	def __init__(self, placa, chassi, renavam, autonomia, reservado = False, quantidadePortas):
		Veiculo.__init__(self, placa, chassi, renavam, autonomia, reservado = False)
		self.__quantidadePortas = __validaQuantPortas(quantidadePortas)

	# Descrição: O método realiza a validação da quantidade de portas, analisando se possui 2 ou 4, se não aciona um erro
	def __validaQuantPortas(self, quantidadePortas):
		if quantidadePortas != 2 or quantidadePortas != 4:
			raise ValidationError("Quantidade inválida, o carro deve possuir 2 ou 4 portas")
		return quantidadePortas

'''
Descrição: Classe que guarda os objetos do tipo Van e é uma classe derivada da Super Classe Veiculo (Classe abstrata) 

Utilização: funciona para diferenciar os tipos de veículos de acordo com suas peculiaridades

Parâmetros:
	Ela recebe todos os parâmetros que veículo recebe, mais a capacidade de pessoas.
'''
class Van(Veiculo):
	def __init__(self, placa, chassi, renavam, autonomia, reservado = False, capacidadePessoas):
		Veiculo.__init__(self, placa, chassi, renavam, autonomia, reservado = False)
		self.__capacidadePessoas = __validaCapacidadePessoas(capacidadePessoas)

		#Descrição: realiza a validação da capacidade de pessoas, analisando se é um número
		def __validaCapacidadePessoas(self, capacidade):
			if capacidade.isdigit():
				return capacidade
			raise ValidationError("A capacidade de pessoas deve ser um número")

'''
Descrição: Classe que guarda os objetos do tipo Utilitario e é uma classe derivada da 
		   Super Classe Veiculo (Classe abstrata) 

Utilização: funciona para diferenciar os tipos de veículos de acordo com suas peculiaridades

Parâmetros:
	Ela recebe todos os parâmetros que veículo recebe, mais o tipo e capacidade da Caçamba
'''
class Utilitarios(Veiculo):
	def __init__(self, placa, chassi, renavam, autonomia, reservado = False, tipoCacamba, capacidadeCacamba):
		Veiculo.__init__(self, placa, chassi, renavam, autonomia, reservado = False)
		self.__tipoCacamba = tipoCacamba
		self.__capacidadeCacamba = capacidadeCacamba

		#Descrição: realiza a validação do tipo de Caçamba, analisando se é uma string
		def __validaTipoCacamba(self, tipo):
			if tipo.isdigit():
				raise ValidationError("Tipo da caçamba não pode ser um número")
			return tipo

		#Descrição: realiza a validação da capacidade da Caçamba, analisando se é um número
		def __validaCapacidadeCacamba(self, capacidade):
			if capacidade.isdigit():
				return capacidade
			raise ValidationError("Capacidade da camçamba deve ser um número")
		
		