 # -*- coding: utf-8 -*-
from VeiculosTipo import *
from VeiculosAbstrato import Veiculo

class VeiculosBD():
	def __init__(self):
		self.__BancoDados = []

	# Descrição: Método que adiciona um veiculo ao banco de dados
	# Recebe como parâmetro tipo de veículo e os parâmetros das classe veículo, sendo o atributo específico de cada tipo representado por "extra"
	def novoVeiculo(self, tipo, fabricante, modelo, extra, autonomia, ano, placa, renavam, chassi, reservado = False ):
		if tipo.lower() == "carro":
			return self.__BancoDados.append(Carro(fabricante, modelo, extra, autonomia, ano, placa, renavam, chassi, reservado))
		elif tipo.lower() == "van":
			return self.__BancoDados.append(Van(fabricante, modelo, extra, autonomia, ano, placa, renavam, chassi, reservado))
		elif tipo.lower() == "ute":
			return self.__BancoDados.append(Utilitario(fabricante, modelo, extra, autonomia, ano, placa, renavam, chassi, reservado))
		else:
			raise ValueError("Não existe veículo do tipo {0}".format(tipo))

	# Descrição: busca um veículo pela placa, chassi ou RENAVAM
	def procurar(self, key):
		key = key.lower()
		for veiculo in self.__BancoDados:
			if key == veiculo.getPlaca() or key == veiculo.getChassi() or key == veiculo.getRenavam():
				return veiculo
		return LookupError("Não existe veículo com esse atributo")

	# Desrição: Busca todos os veículos disponíveis de um certo tipo
	def buscarTipo(self, tipo):
		disponiveis = []
		if tipo.lower() == "carro":
			for veiculo in self.__BancoDados:
				if type(veiculo) is Carro and veiculo.getReservado() == False:
					disponiveis.append(veiculo)
			return disponiveis
		elif tipo.lower() == "van":
			for veiculo in self.__BancoDados:
				if type(veiculo) is Van and veiculo.getReservado() == False:
					disponiveis.append(veiculo)
			return disponiveis
		elif tipo.lower() == "utilitario":
			for veiculo in self.__BancoDados:
				if type(veiculo) is Utilitario and veiculo.getReservado() == False:
					disponiveis.append(veiculo)
			return disponiveis
		else:
			return LookupError("Não existe veículo desse tipo")

	# Descrição: Retorna o número de veículos disponíveis de um certo tipo
	def numVeiculosTipo(self, tipo):
		disponiveis = 0
		if tipo.lower() == "carro":
			for veiculo in self.__BancoDados:
				if type(veiculo) is Carro and veiculo.getReservado() == False:
					disponiveis += 1
			return disponiveis
		elif tipo.lower() == "van":
			for veiculo in self.__BancoDados:
				if type(veiculo) is Van and veiculo.getReservado() == False:
					disponiveis += 1
			return disponiveis
		elif tipo.lower() == "utilitario":
			for veiculo in self.__BancoDados:
				if type(veiculo) is Utilitario and veiculo.getReservado() == False:
					disponiveis += 1
			return disponiveis
		else:
			return LookupError("Não existe veículo desse tipo")


	# Descrição: Cancela a reserva de um certo veículo pela placa
	def cancelarReserva(self, placa):
		for veiculo in self.__BancoDados:
			if veiculo.getPlaca() == placa:
				if veiculo.getReservado() == True:
					veiculo.mudaReserva()
					return "Reserva cancelada"
				else:
					return "Veiculo não está reservado"
		return LookupError("Não existe veículo com placa {0}".format(placa))





