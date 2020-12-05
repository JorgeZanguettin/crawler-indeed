import requests
import json
import sys
import os
import urllib.parse
from datetime import datetime
from bs4 import BeautifulSoup

class CrawlerIndeed():
	def __init__(self):
		self.fileVacancy = self.open_csv_file()

		try:
			position = self.enconde_string_to_url(str(sys.argv[1]))
			city = self.search_city(str(sys.argv[2]))
		except:
			self.send_log_system('ERROR', 'Syntax de execução incorreta. Correta : python indeed.py Cargo Cidade')
			quit()

		self.search_job(position, city)
		self.fileVacancy.close()

	def send_log_system(self, type_message, message):
		print (f'[ {type_message} ] {message}')

	def search_city(self, input_city):
		options = {}

		apiUrl = 'https://autocomplete.indeed.com/api/v0/suggestions/location?country=BR&language=pt&count=10&formatted=1&query={}&useEachWord=false&useAltLabel=false&sessionId=99bdeee0-0384-11eb-bb1c-d3e38e5e923e&seqId=7&page=homepage&ctk=1ef88foe5qo3m800&merged=true'.format(input_city)

		print ('DIGITE O NUMERO DA CIDADE DESEJADA OU PRESSIONE 0 PARA SAIR')		
		for i, cities in enumerate(json.loads(requests.get(apiUrl).content.decode('utf-8'))):
			options[i+1] = cities['suggestion']
			print ('{} - {}'.format(i+1, cities['suggestion']))

		while True:
			try:
				option = int(input("\nOpção : "))

				if int(option) == 0:
					break
				elif option < 10 and option > 0:
					return self.enconde_string_to_url(options[option])
				else:
					print ("Digite uma opção valida")
			except:
				print ("Digite uma opção valida")

		return option

	def search_job(self, position, city):
		page = 1

		urlFind = 'https://www.indeed.com.br/empregos?q={}&l={}'.format(position, city)
		while True:
			requestFind = requests.get(urlFind)
			objBs4Find = BeautifulSoup(requestFind.content, 'html.parser')
			vacancyList = objBs4Find.find_all('div', {"data-tn-component" : "organicJob"})

			for vagaProps in vacancyList:
				objBs4Position = BeautifulSoup(str(vagaProps), 'html.parser')
				
				dictVacancy = self.get_job_dict(
					self.handle_string(objBs4Position.find("a", {"data-tn-element" : "jobTitle"})), 
					self.handle_string(objBs4Position.find("span", {"class" : "company"})), 
					self.handle_string(objBs4Position.select_one('div.summary ul')),
					'https://www.indeed.com.br' + str(objBs4Position.find("a", {"data-tn-element" : "jobTitle"})['href']),
					self.handle_string(objBs4Position.select_one('div.result-link-bar span'))
				)

				self.send_job_to_file(dictVacancy)

			findNextPage = objBs4Position.find('a', {'aria-label' : 'Próxima'})
			if findNextPage != None:
				page+=1

				urlFind = 'https://www.indeed.com.br' + str(findNextPage['href'])
			else:
				break

	def send_job_to_file(self, dictVacancy):
		self.send_log_system('DEGUB', 'Vaga Coletada - {}'.format(dictVacancy['titulo_vaga']))
	
		allValuesToWrite = [dictVacancy[key] for key in dictVacancy]
		rowToWrite = str(';'.join(allValuesToWrite)) + '\n'
		self.fileVacancy.write(rowToWrite)

	def open_csv_file(self):
		if 'vagas.csv' not in os.listdir('./'):
			fileVacancy = open('./vagas.csv', 'a+', encoding='utf-8')
			fileVacancy.write('titulo_vaga;nome_empresa;resumo_vaga;link_vaga;vaga_postada_há;data_coleta\n')
		else:
			fileVacancy = open('./vagas.csv', 'a+', encoding='utf-8')

		return fileVacancy

	def handle_string(self, string):
		if string != None:
			return (str(string.text).replace('\n','').replace(';','.').strip())
		else:
			return ''

	def enconde_string_to_url(self, string):
		return str(urllib.parse.quote_plus(string)).strip()

	def get_job_dict(self, tituloVaga, nomeEmpresa, resumoVaga, linkVaga, vagaPostadaHa):
		return {
			'titulo_vaga' : tituloVaga,
			'nome_empresa' : nomeEmpresa,
			'resumo_vaga' : resumoVaga,
			'link_vaga' : linkVaga,
			'vaga_postada_há' : vagaPostadaHa,
			'data_coleta' : str(datetime.now())
		}

CrawlerIndeed()