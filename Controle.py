 # -*- coding: utf-8 -*-
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
    def numVeiculosDisponiveis(self):
            return self.__BancoDeDados.numVeiculos()

    # Descrição: Recupera o número de veículos não reservados de um determinado
    def numVeiculosDisponiveisTipo(self, tipo):
            return self.__BancoDeDados.numVeiculosTipo(tipo)

    # Descrição: Devolve uma lista formada por todos os veículos disponíveis de um certo tipo
    def veiculosDisponiveisTipo(self, tipo):
            return self.__BancoDeDados.buscarTipo(tipo)

    # Descrição: Insere um novo veículo no banco de dados
    def inserirVeiculo(self, tipo, fabricante, modelo, extra, autonomia, ano, placa, renavam, chassi, reservado):
            return self.__BancoDeDados.novoVeiculo(tipo, fabricante, modelo, extra, autonomia, ano, placa, renavam, chassi, reservado)

    # Descrição: Busca um veículo pela placa, chassi ou renavam
    def procurarVeiculo(self, key):
            return self.__BancoDeDados.procurar(key)

    # Descrição: Realiza a reserva do veículo pelo chassi, placa ou RENAVAM
    def reservarVeiculo(self, key):
            return self.__BancoDeDados.reservar(key)

    # Descrição: Cancela a reserva do veículo pelo chassi, placa ou RENAVAM
    def cancelarVeiculo(self, key):
            return self.__BancoDeDados.cancelarReserva(key)

    # Descrição: Carrega um arquivo txt no banco de dados
    def carregarBancoDados(self, arquivo):
            arquivoVeiculos = open(arquivo, "r")
            arquivoVeiculos.readline()

            for veiculo in arquivoVeiculos:
                    veiculo = veiculo.split()
                    self.inserirVeiculo(veiculo[0], veiculo[1], veiculo[2], veiculo[3], veiculo[4], veiculo[5], veiculo[6], veiculo[7], veiculo[8], veiculo[9])

            arquivoVeiculos.close()

    # Descrição: Salva as informações do banco de dados em um arquivo txt
    def salvarBancoDados(self, arquivo):
            arquivoVeiculos = open(arquivo, "w")
            arquivoVeiculos.write("tipo    fabricante    modelo    portas/capacidade    autonomia    ano    placa    renavam    chassi \n")

            for veiculo in self.__BancoDeDados.listaVeiculos():
                    arquivoVeiculos.write(veiculo)
                    arquivoVeiculos.write("\n")

            arquivoVeiculos.close()



                
                
