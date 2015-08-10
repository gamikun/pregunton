# -*- coding: utf8 -*-
import re
from datetime import datetime as dt
from datetime import timedelta
import math
import random
import hashlib
import time
import sys


dupli_answer = [
	'otra vez?',
	'ya te dije que no?',
	'y dale con lo mismo',
	'ya dijiste eso',
]

programming_languages = [
	'C#', 'Visual Basic', 'Python',
	'Scala', 'Java', 'Objective-C',
	'C', 'C++', 'D', 'Red', 'Rust',
	'Javascript', 'Ruby', 'LISP',
]

colors = {
	'el cielo': 'azul de día y negro de noche',
	'las nubes': 'blancas, pero a veces varían de acuerdo al clima',
	'las rosas': 'blancas, rosas, rojas, amarillas y creo que azules',
	'tus ojos': 'cafeses',
	'el agua': 'se supone que es transparente, pero en el mar se ve azul',
}

month_names = {
	'enero': 1, 'febrero': 2, 'marzo': 3,
	'abril': 4, 'mayo': 5,    'junio': 6,
	'julio': 7, 'agosto': 8,  'septiembre': 9,
	'octubre': 10, 'noviembre': 11, 'diciembre': 12,
}

hashers = {
	'md5': lambda x: hashlib.md5(x).hexdigest(),
	'sha1': lambda x: hashlib.sha1(x).hexdigest(),
}

asked = []

learnt_data = {}

class are:
	def __init__(self, pattern):
		self.re = re.compile(pattern)

def reco(pattern):
	return are(pattern)

def time_left(m):
	name = m.group(1).strip()
	now = dt.now()
	if name.startswith('navida'):
		return dt(year=now.year, month=12, day=24) - now
	if name.startswith('ano nuevo'):
		return dt(year=now.year + 1, month=1, day=1)
	mm = re.match('el\\s(\d{1,2})\\sde\\s(enero|febrero|marzo|abril|mayo|junio|julio'
		        + '|agosto|septiembre|octubre|noviembre|diciembre)', name)
	if not mm is None:
		month = month_names[mm.group(2)]
		day = int(mm.group(1))
		the_date = dt(year=now.year, month=month, day=day)
		if now > the_date:
			the_date = dt(year=now.year + 1, month=month, day=day)
		return the_date - now;

	mm = re.match('el\\selcumple(?:anos)?\\sde(.+)', fill_name)
	if not mm is None:
		return "no sé cuando es"
	return "mucho tiempo"

def who_is(m):
	who = m.group(1)
	key = 'quien es %s' % who
	if key in learnt_data:
		return learnt_data[key]
	name = raw_input('no lo sé, quién es? ').strip()
	if name != '':
		if name.startswith('mi '):
			name = name.replace('mi ', 'tu ')
		elif name.startswith('tu '):
			name = name.replace('tu ', 'mi ')
		learnt_data[key] = name
		return "oh ya veo"
	else:
		print "no me digas pues :("

def fill_name(m):
	key = 'tu nombre'
	name = m.group(1)
	if key in learnt_data:
		return "ya lo sabía"
	learnt_data[key] = name
	return "mucho gusto %s" % name

def asked_price(m):
	prefix = m.group(1)
	subject = m.group(2)

	if subject == 'iphone':
		return "Como 10 mil pesos los iPhone 6"
	else:
		return "No sé, tal vez cueste mucho dinero %s %s"\
			 % (prefix, subject,)

def tell_programming_language(m=None):
	return 

def what2study(m):
	from quizes import questudiar
	return questudiar.start_quiz()

def resolve_host(m):
	import socket
	try:
		socket.gethostbyname(m.group(1))
		return "sí"
	except:
		return "no"

def bye(m):
	print("hasta luego")
	time.sleep(1)
	sys.exit(0)


def dollar(m):
	import requests

	if not 'precio dolar' in learnt_data:
		print("déjame calcularlo...")
		response = requests.get(
			"http://download.finance.yahoo.com/d/quotes.csv?s=USDMXN=X&f=l1&e=.cs"
		)
		precio = float(response.content)\
				if response.status_code == 200\
				else None
		learnt_data['precio dolar'] = precio
	else:
		precio = learnt_data['precio dolar']

	if not precio is None:
		return "en $%2.f pesos" % precio

	return "no lo sé"

questions = [
	(1, set(['hola', 'oli', 'oli', 'holi']),
		['hola', 'hola que tal?', 'keubole', 'qué pasa?']),
	(2, 'hey', 'que onda?'),
	(3, reco('(cual es tu nombre|(como )?te llamas)\\?'), lambda: 'gamaliel'),
	(4, 'estoy aburrido', 'qué quieres hacer?'),
	(5, 'vamos al cine', 'vamos'),
	(6, 'hello world', 'en qué lenguaje de programación?'),
	(7, 'que calor', 'donde vives?'),
	(8, 'te apestan los pies?', 'no, soy una computadora'),
	(9, 'cuantos años tienes?', 'vamos'),
	(10, 'que anime te gusta?', 'naruto'),
	(11, 'cual es tu color favorito?', 'verde'),
	(12, 'dime un trabalenguas', 'me da weba'),
	(13, 'comete un trusco', 'esa frase es de mi madre, jaja'),
	(14, 'cual es tu facebook?', 'http://facebook.com/soygama, agrégame'),
	(15, 'tu pelicula favorita?', 'la era del hielo 2'),
	(16, 'que haces?', 'tirando barra, machín'),
	(17, 'chilenos', 'la wea fome qliao'),
	(18, 'argentina', 'no me rompás la pelota boludo'),
	(19, 'pitorrito', 'así que conoces al baitan'),
	(20, 'me ando meando', 'córrele al baño'),
	(21, 'el cielo es azul', 'y los árboles son verdes'),
	(22, 'weon qliao', 'ah eres chileno?'),
	(23, 'preguntame algo', 'tienes carro?'),
	(24, 'que desayunaste?', 'huevo, qué más?'),
	(25, 'tengo sueño', 'y por qué no duermes?'),
	(26, 'quiero dinero', 'vende aguacates'),
	(27, 'dame dinero', 'por qué lo haría?'),
	(28, 'ando viendo la novela', 'cuál?'),
	(29, 'tienes carro?', 'sí, un chevy 99 color plata'),
	(30, 'hay que tomar', 'cerveza, vino o vodka?'),
	(31, 'mexico', 
		['tacos?', 'charros?', 'fútbol', 'matraca?',
		 'guacamole?', 'presidente enrique?', 'salsa?',
		 'burritos?', 'quesadillas?', 'garnachas?',
		 'corrupción?',]
		),
	(32, 'me duele', 'qué te duele?'),
	(33, 'steve jobs', 'lo dices porque te gusta apple o lo odias?'),
	(34, 'bill gates', 'te gusta microsoft o puro pedo?'),
	(35, 'echame una manita', 'de la buena o de la mala?'),
	(36, 'vamos a comer', 'qué quieres comer?'),
	(37, 'python', 'este programa está hecho en ese lenguaje'),
	(38, 'alma garcía', 'tepetlanco? la morra emo de edesarrollos?'),
	(39, 'dónde vives?', 'en Hermosillo'),
	(40, 'eres mexicano?', 'asina es'),
	(41, 'apestoso', 'no tanto como tus patas'),
	(42, 'payaso', 'en verdad soy un payaso, pero qué le voy a hacer?'),
	(43, 'drogas', 'marihuana?'),
	(44, 'noticias', 'normalmente hay puras malas noticias'),
	(45, 'facebook', 'estás conectado?'),
	(46, 'a la monda', 'así se llama un grupo coahuila'),
	(47, reco('(((?:me (?:das|dices))|dame) la h?ora|(ke?|que) h?ora (?:es|seran?))\\??'),
		 lambda x: dt.now().strftime('%H:%S')),
	(48, 'no mames', 'no mamo, tú sí?'),
	(49, reco('(?:ke?|qu?e?) (?:opinas|piensas) de (((las?|el|los?)\\s)?([^\?]+))\\?*'),
		 lambda x: 'no tengo nada qué decir de %s' % x.group(1)
		),
	(50, reco('(?:[kc]uanto|(?:que|ke?) tanto) falta para ([^\\?]+)\\?*'), time_left),
	(51, reco('(?:(?:qu|k)ien) te (?:creo|hizo)\\?*'), 'Gamaliel Espinoza Macedo'),
	(52, reco('(?:(?:qu|k)ien) es ([^\\?]+)\\?*'), who_is),
	(53, reco('(?:mi nombre es|me llamo|llamame) (.+)'), fill_name),
	(54, reco('(?:de )?(?:(?:que|ke?) color )(?:es|son )([^\\?]+)\\?*'),
		 lambda x: colors[x.group(1)] if x.group(1) in colors else 'no lo sé'),
	(55, 'hermosillo', ['carne asada?', 'machaca?', 'coyotas', 'chimichangas?']),
	(56, reco(r'(?:da|di)me el (md5|sha1) de (.+)'),
		lambda x: hashers[x.group(1)](x.group(2))),
	(56, reco(r'[ck]uanto cuesta (una?|las?|los?) ([^\?]+)\?*'), asked_price),
	(57, reco(r'(?:qu|ke?) (?:se?ra bu?e?no|podria|pu?e?do) e?studiar\?*'), what2study),
	(58, reco(r'existe el dominio (\w+(?:\.\w+)+)\?*'), resolve_host),
	(59, reco(r'(adios|bye|al rato|ya me voy)'), bye),
	(60, reco(r'(?:en )?cua[nt]{2}o e?sta el doll?ar?'), dollar),
]

def normalize_text(text):
	if text is None: return ""
	return text.strip().lower()\
		 .replace("á", "a").replace("é", "e")\
		 .replace("í", "i").replace("ó", "o")\
		 .replace("ú", "u").replace("ü", "u")\
		 .replace('ñ', "n")\

def random_element(array):
	return array[random.randint(0, len(array) - 1)]

while 1:
	answer = None
	q = normalize_text(raw_input("yo: "))
	for qs in questions:
		qid, question, answer = qs
		if isinstance(question, set):
			if q in question:
				if isinstance(question, str):
					answer = answer
				else:
					answer = random_element(answer)
				break
		if isinstance(question, are):
			m = question.re.match(q)
			if not m is None:
				if isinstance(answer, str):
					answer = answer
				else:
					answer = answer(m)
				break
		if isinstance(question, str):
			if question == q:
				if isinstance(answer, str):
					answer = answer
				else:
					answer = random_element(answer)
				break
	if answer is None:
		answer = "que?"
	print("ella: %s" % answer)
	