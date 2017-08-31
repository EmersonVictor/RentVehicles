 # -*- coding: utf-8 -*-

'''
Descrição: A classe Veiculo é uma classe abstrata que funciona para construir os tipos de veículo

Utilização: A Classe realiza validações dos valores padrões

Parâmetros:
	Placa: 3 letras seguidas de 4 números (ex: KKK0000)
	Chassi: Mistura de letras e números seguindo o formato 3TT333TT33T333333 (3 = Números/ T = Letras)
	Renavam: 9 dígitos inteiros
	Autonomia: Número inteiro medido em Km/L
	Reservado: Recebe True, para não reservado, ou False, para reservado
'''
class Veiculo ():
	def __init__(self, placa, chassi, renavam, autonomia, reservado = False):
	    self.__placa = __validaPlaca(placa)
	    self.__chassi = __validaChassi(chassi)
	    self.__renavam = __validaRenavam(renavam)
	    self.__autonomia = autonomia
	    self.__reservado = __validaReservado(reservado)

	    
	    # Descrição: O método __validaPlaca realiza a validação da placa, analisando se o string está no formato correto
	    def __validaPlaca(self, placa):
	    	if not (placa[0:3].isdigit()) and placa[3:7].isdigit() and len(placa) == 8:
	    		return placa

	    	raise ValidationError("Placa {0} não segue o formato".format(placa))

	    # Descrição: O método __validaChassi realiza a validação do chassi, analisando se o string está no formato correto
	    def __validaChassi(self, chassi):
	    	for x in range(0, len(chassi)):
	    		if x == 1 or x == 2 or x == 6 or x == 7 or x == 10:
	    			if chassi[x].isdigit():
	    				raise ValidationError("Chassi {0} não segue o formato".format(chassi))
	    		else: 
	    			if not(chassi[x].isdigit()):
	    				raise ValidationError("Chassi {0} não segue o formato".format(chassi))
	    	return chassi

	    # Descrição: O método __validaRenavam realiza a validação do RENAVAM, analisando se todos os digitos do string são números e se possui o tamanho correto
	    def __validaRenavam(self, renavam):
	    	if isinstance(renavam, int) and len(str(renavam)) == 9:
	    		return renavam
	    	raise ValidationError("Renavam {0} não segue o formato".format(renavam))

	    # Descrição: O método __validaReservado realiza a validação do valor recebido em reservado, analisando se é um valor booleano
	    def __validaReservado(self, reservado):
	    	if isinstance(reservado, bool):
	    		return reservado
	    	raise TypeError("Reservado deve ser um valor booleano")