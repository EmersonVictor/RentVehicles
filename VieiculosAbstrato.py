 # -*- coding: utf-8 -*-

'''
Descrição: A classe Veiculo é uma classe abstrata que funciona para construir os tipos de veículo

Utilização: A Classe realiza validações dos valores padrões

Parâmetros:
	Fabricante: String que representa o fabricante do veículo
	Modelo: string representando o modelo do veículo
	Autonomia: Número inteiro medido em Km/L
	Ano: Interiro formado por 4 digitos
	Placa: 3 letras seguidas de 4 números (ex: KKK0000)
	Renavam: 9 dígitos inteiros
	Chassi: Mistura de letras e números seguindo o formato 3TT333TT33T333333 (3 = Números/ T = Letras)
	Reservado: Recebe True, para não reservado, ou False, para reservado
'''
class Veiculo ():
	def __init__(self, fabricante, modelo, autonomia, ano, placa, renavam, chassi, reservado = False):
	    self.__fabricante = fabricante
	    self.__modelo = modelo
	    self.__autonomia = autonomia
	    self.__ano = __validaAno(ano)
	    self.__placa = __validaPlaca(placa)
	    self.__renavam = __validaRenavam(renavam)
	    self.__chassi = chassi
	    self.__reservado = __validaReservado(reservado)

	    
	    # Descrição: O método __validaPlaca realiza a validação da placa, analisando se o string está no formato correto
	    def __validaPlaca(self, placa):
	    	if not (placa[0:3].isdigit()) and placa[3:7].isdigit() and len(placa) == 8:
	    		return placa
	    	raise ValidationError("Placa {0} não segue o formato".format(placa))

	    # Descrição: O método __validaRenavam realiza a validação do RENAVAM, analisando se todos os digitos do string são números e se possui o tamanho correto
	    def __validaRenavam(self, renavam):
	    	if renavam.isdigit() and len(str(renavam)) == 9:
	    		return int(renavam)
	    	raise ValidationError("Renavam {0} não segue o formato".format(renavam))

	    # Descrição: O método __validaReservado realiza a validação do valor recebido em reservado, analisando se é um valor booleano
	    def __validaReservado(self, reservado):
	    	if reservado.lower() == "true" or reservado.lower() == "false":
	    		return bool(reservado)
	    	raise TypeError("Reservado deve ser um valor booleano")

	    # Descrição: O método __validaAno realiza a validação do ano recebido, analisando se é um inteiro formado por 4 digitos
	    def __validaAno(self, ano):
	    	if ano.isdigit() and len(str(ano)) == 4:
	    		return Int(ano)
	    	raise ValidationError("{0} não segue o formato correto".format(ano))