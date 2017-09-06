 # -*- coding: utf-8 -*-
from VeiculosTipo import *
from VeiculosAbstrato import Veiculo
from VeiculosBD import VeiculosBD

'''
Descrição: A classe Controle é utilizada para realizar as ações que o usuário desejar com o banco de dados

Utilização: A classe vai receber as informações do usuário e realizar a chamada dos seus métodos para realizar as ações

Parâmetro: A classe não recebe nenhum parâmetro e inicializa com um objeto do tipo VeiculosBD
'''

class Controle():

	def __init__(self):
		self.__BancoDeDados = VeiculosBD()
	
	# Descrição: Recupera o número de veículos não reservados
	def veiculosDisponiveis(self):
		return self.__BancoDeDados.numVeiculos()

	# Descrição: Recupera o número de veículos não reservados de um determinado
	def veiculosDisponiveisTipo(self, tipo):
		return self.__BancoDeDados.numVeiculosTipo(tipo)

	def inserirVeiculo(self, tipo, fabricante, modelo, extra, autonomia, ano, placa, renavam, chassi, reservado):
		return self.__BancoDeDados.novoVeiculo(tipo, fabricante, modelo, extra, autonomia, ano, placa, renavam, chassi, reservado)

	# Descrição: Realiza a reserva do veículo pelo chassi, placa ou RENAVAM
	def reservarVeiculo(self, key):
		return self.__BancoDeDados.reservar(key)

	# Descrição: Cancela a reserva do veículo pelo chassi, placa ou RENAVAM
	def cancelarVeiculo():
		return self.__BancoDeDados.cancelarReserva()

	# Descrição: Carrega um arquivo txt no banco de dados
	def carregarBancoDados():

	# Descrição: Salva as informações do banco de dados em um arquivo txt
	def salvarBancoDados():