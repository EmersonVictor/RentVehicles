 # -*- coding: utf-8 -*-
from VeiculosAbstratos import Veiculo

'''
Descrição:

Utilização:

Parâmetro:

'''
class Carro(Veiculo):
	def __init__(self, placa, chassi, renavam, autonomia, reservado = False, quantidadePortas):
		Veiculo.__init__(self, placa, chassi, renavam, autonomia, reservado = False)
		self.__quantidadePortas = __validaQuantPortas(quantidadePortas)

	def __validaQuantPortas(self, quantidadePortas):
		if quantidadePortas != 2 or quantidadePortas != 4:
			raise ValidationError("Quantidade inválida, o carro deve possuir 2 ou 4 portas")
		return quantidadePortas

'''
Descrição:

Utilização:

Parâmetro:

'''
class Van(Veiculo):
	def __init__(self, placa, chassi, renavam, autonomia, reservado = False, capacidadePessoas):
		Veiculo.__init__(self, placa, chassi, renavam, autonomia, reservado = False)
		self.__capacidadePessoas = capacidadePessoas

'''
Descrição:

Utilização:

Parâmetro:

'''
class Utilitarios(Veiculo):
	def __init__(self, placa, chassi, renavam, autonomia, reservado = False, tipoCacamba, capacidadeCacamba):
		Veiculo.__init__(self, placa, chassi, renavam, autonomia, reservado = False)
		self.__tipoCacamba = tipoCacamba
		self.__capacidadeCacamba = capacidadeCacamba
		
		