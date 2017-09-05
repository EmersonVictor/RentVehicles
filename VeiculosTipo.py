 # -*- coding: utf-8 -*-
from VeiculoAbstrato import Veiculo

'''
Descrição: Classe que guarda os objetos do tipo Carro e é uma classe derivada da Super Classe Veiculo (Classe abstrata) 

Utilização: funciona para diferenciar os tipos de veículos de acordo com suas peculiaridades

Parâmetros:
	Ela recebe todos os parâmetros que veículo recebe, mais a quantidade de portas que possui, podendo ser 2 ou 4.
'''
class Carro(Veiculo):
	def __init__(self, fabricante, modelo, quantidadePortas, autonomia, ano, placa, renavam, chassi, reservado = False):
		Veiculo.__init__(self, fabricante, modelo, autonomia, ano, placa, renavam, chassi, reservado = False)
		self.__quantidadePortas = self.__validaQuantPortas(quantidadePortas)

	def __repr__(self):
		return "Carro - {0},{1},{2},{3} - {4} - {5},{6},{7} - {8}".format(self.getFabricante(), self.getModelo(), self.getAno(), self.getAutonomia(), self.__quantidadePortas, self.getPlaca(), self.getRenavam(), self.getChassi(), self.getReservado())

	# Descrição: O método realiza a validação da quantidade de portas, analisando se possui 2 ou 4, se não aciona um erro
	def __validaQuantPortas(self, quantidadePortas):
		if int(quantidadePortas) != 2 and int(quantidadePortas) != 4:
			raise ValueError("Quantidade inválida, o carro deve possuir 2 ou 4 portas")
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
		self.__capacidadePessoas = self.__validaCapacidadePessoas(capacidadePessoas)

	def __repr__(self):
		return "Van - {0},{1},{2},{3} - {4} - {5},{6},{7} - {8}".format(self.getFabricante(), self.getModelo(), self.getAno(), self.getAutonomia(), self.__capacidadePessoas, self.getPlaca(), self.getRenavam(), self.getChassi(), self.getReservado())


	#Descrição: realiza a validação da capacidade de pessoas, analisando se é um número
	def __validaCapacidadePessoas(self, capacidade):
		if capacidade.isdigit():
			return int(capacidade)
		raise ValueError("A capacidade de pessoas deve ser um número")



'''
Descrição: Classe que guarda os objetos do tipo Utilitario e é uma classe derivada da 
		   Super Classe Veiculo (Classe abstrata) 

Utilização: funciona para diferenciar os tipos de veículos de acordo com suas peculiaridades

Parâmetros:
	Ela recebe todos os parâmetros que veículo recebe, mais a capacidade da Caçamba
'''
class Utilitario(Veiculo):
	def __init__(self, fabricante, modelo, capacidadeCacamba, autonomia, ano, placa, renavam, chassi, reservado = False):
		Veiculo.__init__(self, fabricante, modelo, autonomia, ano, placa, renavam, chassi, reservado = False)
		self.__capacidadeCacamba = self.__validaCapacidadeCacamba(capacidadeCacamba)

	def __repr__(self):
		return "Utilitário - {0},{1},{2},{3} - {4} - {5},{6},{7} - {8}".format(self.getFabricante(), self.getModelo(), self.getAno(), self.getAutonomia(), self.__capacidadeCacamba, self.getPlaca(), self.getRenavam(), self.getChassi(), self.getReservado())

	#Descrição: realiza a validação da capacidade da Caçamba, analisando se é um número
	def __validaCapacidadeCacamba(self, capacidade):
		if capacidade.isdigit():
			return int(capacidade)
		raise ValueError("Capacidade da caçamba deve ser um número")
		
		
