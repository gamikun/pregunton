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

months = [
	'no', 'enero', 'febrero', 'marzo',
	'abril', 'mayo', 'junio', 'julio',
	'agosto', 'septiembre', 'octubre',
	'noviembre', 'diciebre',
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

who_is_index = {
	'harry potter': 'un mago',
}

hashers = {
	'md5': lambda x: hashlib.md5(x).hexdigest(),
	'sha1': lambda x: hashlib.sha1(x).hexdigest(),
}

predefined_dates = {
	'cumple bill gates': dt(year=1955, month=10, day=28),
	'cumple steve jobs': dt(year=1955, month=2,  day=24),
	'cumple gamaliel': dt(year=1988, month=2, day=12),
	'navidad': dt(year=2000, month=12, day=25),
	'ano nuevo': dt(year=2000, month=1, day=1),
}

asked = []

learnt_data = {}

class are:
	def __init__(self, pattern):
		self.re = re.compile(pattern)

class stwith(object):
	__slots__ = ['variants']
	def __init__(self, variants=[]):
		self.variants = variants

def reco(pattern):
	return are(pattern)

def time_left(m):
	name = m.group(1).strip()
	now = dt.now()
	if name.startswith('navida'):
		return dt(year=now.year, month=12, day=24) - now
	if name.startswith('ano nuevo'):
		return dt(year=now.year + 1, month=1, day=1)
	if name.startswith('el fin del mundo'):
		return "Nadie lo sabe"
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
	if who in who_is_index:
		return who_is_index[who]
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

def when(m):
	phrase = m.group(1)
	if prhase.startswith('es '):
		return when_is(word[3:])
	return "cuando qué?"

def when_is_birthday(m):
	person = m.group(1)
	key = 'cumple %s' % person
	date = predefined_dates.get(key, None)
	if not date is None:
		return date
	if key in learnt_data:
		return learnt_data[key]
	return "no sé el cumpleaños de %s" % person

def when_is_holiday(m):
	holiday = m.group(1)
	if holiday in predefined_dates:
		hday = predefined_dates[holiday]
		return "el %d de %s" \
			 % (hday.day, months[hday.month])
	return "no sé cuando es %s" % holiday

def weather_today(m):
	import requests
	url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=Hermosillo&mode=json&units=metric&cnt=1"
	response = requests.get(url)
	if response.status_code == 200:
		import json
		obj = json.loads(response.content)
		temp = obj.get('list')[0].get('temp').get('day')
		return "está a %.1f ºC" % float(temp)
	else:
		return "no estoy seguro"

def como_matar(w):
	if w.startswith("el gusano"):
		return "el gusano%s" % (" se mata así" * 3)
	return "solo golpéalo hasta morir"

def como(w):
	if w.startswith("matar "):
		return como_matar(w[6:])
	if w.startswith("se mata "):
		return como_matar(w[8:])
		
	return "cómo qué?"

questions = [
	(1, set(['hola', 'oli', 'oli', 'holi']),
		['hola', 'hola que tal?', 'keubole', 'qué pasa?']),
	(2, u'hey', 'que onda?'),
	(3, reco('(cual es tu nombre|(como )?te llamas)\\?'), lambda: 'gamaliel'),
	(4, u'estoy aburrido', 'qué quieres hacer?'),
	(5, u'vamos al cine', 'vamos'),
	(6, u'hello world', 'en qué lenguaje de programación?'),
	(7, u'que calor', 'donde vives?'),
	(8, u'te apestan los pies?', 'no, soy una computadora'),
	(9, u'cuantos años tienes?', 'vamos'),
	(10, u'que anime te gusta?', 'naruto'),
	(11, u'cual es tu color favorito?', 'verde'),
	(12, reco(r'dime (una?)'), 'no sé'),
	(12, u'dime un trabalenguas', 'me da weba'),
	(13, u'comete un trusco', 'esa frase es de mi madre, jaja'),
	(14, u'cual es tu facebook?', 'http://facebook.com/soygama, agrégame'),
	(15, u'tu pelicula favorita?', 'la era del hielo 2'),
	(16, u'que haces?', 'tirando barra, machín'),
	(17, u'chilenos', 'la wea fome qliao'),
	(18, u'argentina', 'no me rompás la pelota boludo'),
	(19, u'pitorrito', 'así que conoces al baitan'),
	(20, u'me ando meando', 'córrele al baño'),
	(21, u'el cielo es azul', 'y los árboles son verdes'),
	(22, u'weon qliao', 'ah eres chileno?'),
	(23, u'preguntame algo', 'tienes carro?'),
	(24, u'que desayunaste?', 'huevo, qué más?'),
	(25, u'tengo sueño', 'y por qué no duermes?'),
	(26, u'quiero dinero', 'vende aguacates'),
	(27, u'dame dinero', 'por qué lo haría?'),
	(28, u'ando viendo la novela', 'cuál?'),
	(29, u'tienes carro?', 'sí, un chevy 99 color plata'),
	(30, u'hay que tomar', 'cerveza, vino o vodka?'),
	(31, u'mexico', 
		('tacos?', 'charros?', 'fútbol', 'matraca?',
		 'guacamole?', 'presidente enrique?', 'salsa?',
		 'burritos?', 'quesadillas?', 'garnachas?',
		 'corrupción?',)
		),
	(32, u'me duele', 'qué te duele?'),
	(33, u'steve jobs', 'lo dices porque te gusta apple o lo odias?'),
	(34, u'bill gates', 'te gusta microsoft o puro pedo?'),
	(35, u'echame una manita', 'de la buena o de la mala?'),
	(36, u'vamos a comer', 'qué quieres comer?'),
	(37, u'python', 'este programa está hecho en ese lenguaje'),
	(38, u'alma garcía', '<3'),
	(39, u'dónde vives?', 'en Hermosillo'),
	(40, u'eres mexicano?', 'asina es'),
	(41, u'apestoso', 'no tanto como tus patas'),
	(42, u'payaso', 'en verdad soy un payaso, pero qué le voy a hacer?'),
	(43, u'drogas', 'marihuana?'),
	(44, u'noticias', 'normalmente hay puras malas noticias'),
	(45, u'facebook', 'estás conectado?'),
	(46, u'a la monda', 'así se llama un grupo de coahuila'),
	(47, reco('(((?:me (?:das|dices))|dame) la h?ora|(ke?|que) h?ora (?:es|seran?|traes?))\\??'),
		 lambda x: dt.now().strftime('%H:%S')),
	(48, 'no mames', 'no mamo, tú sí?'),
	(49, reco('(?:ke?|qu?e?) (?:opinas|piensas|me dices) de (((las?|el|los?)\\s)?([^\?]+))\\?*'),
		 lambda x: 'no tengo nada qué decir de %s' % x.group(1)
		),
	(50, reco('(?:[kc]uanto|(?:que|ke?) tanto) falta para ([^\\?]+)\\?*'), time_left),
	(51, reco('(?:(?:qu|k)ien) te (?:creo|hizo)\\?*'), 'Gamaliel Espinoza Macedo'),
	(52, reco('(?:(?:qu|k)ien) es ([^\\?]+)\\?*'), who_is),
	(53, reco('(?:mi nombre es|me llamo|llamame) (.+)'), fill_name),
	(54, reco('(?:de )?(?:(?:que|ke?) color )(?:es|son )([^\\?]+)\\?*'),
		 lambda x: colors[x.group(1)] if x.group(1) in colors else 'no lo sé'),
	(55, u'hermosillo', ['carne asada?', 'machaca?', 'coyotas', 'chimichangas?']),
	(56, reco(r'(?:da|di)me el (md5|sha1) de (.+)'),
		lambda x: hashers[x.group(1)](x.group(2))),
	(56, reco(r'[ck]uanto [ck]uestan? (una?|las?|los?) ([^\?]+)\?*'), asked_price),
	(57, reco(r'(?:qu|ke?) (?:se?ri?a bu?e?no|podria|pu?e?do) e?studiar\?*'), what2study),
	(58, reco(r'existe el dominio (\w+(?:\.\w+)+)\?*'), resolve_host),
	(59, reco(r'(adios|bye|al rato|ya me voy)'), bye),

	# Valor del dólar
	(60, reco(r'(?:en\s)?[ck]ua[nt]{2}o\se?sta\sel\sdoll?ar?\?*'), dollar),
	(61, reco(r'(esto es|es esto) una pregunta\?'), 'sí'),

	# CUANDO CUMPLE AÑOS / CUANDO ES EL CUMPLEAÑOS
	(None, reco(r'^[ck]uando\s+(?:es\s+el\s+[ck]u?mple(?:anos)?\s+de|[ck]umple\s+anos)\s+([^\?]+)\?*'),
		when_is_birthday
		),
	# CUANDO ES X día del año
	(None, reco(r'^[ck]uando\s+(?:es)\s+([^\?]+)\?*'), when_is_holiday),

	# CLIMA
	(0, reco(r'^(?:[ck]omo|(?:que|ke?)\s+tal)\s+(?:anda|esta)\s+el\s+clima(?:\s+hoy)?\?*'), weather_today),
	(0, reco(r'^a\s+[ck]ua[nt]{1,2}o(?:s?\s+grados)?\s+e?sta?mo?s\?*'), weather_today),

	# COMO (primero experimental de arbol completo),
	(0, stwith(variants=['komo ', 'como ']), como),

]

question_counter = [x for x in range(len(questions))]

def normalize_text(text):
	if text is None: return ""
	return text.strip().lower()\
		 .replace("á", "a").replace("é", "e")\
		 .replace("í", "i").replace("ó", "o")\
		 .replace("ú", "u").replace("ü", "u")\
		 .replace('ñ', "n")\

def random_element(array):
	return array[random.randint(0, len(array) - 1)]

"""def handle_answer(answer, question=None):
	if isinstance(answer, str):
		return str
	if hasattr(answer, '__call__'):
		return """


if __name__ == '__main__':
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
			if isinstance(question, stwith):
				for word in question.variants:
					if q.startswith(word):
						if hasattr(answer, '__call__'):
							answer = answer(q[len(word):])
						break

		if answer is None:
			answer = "que?"
		print("ella: %s" % answer)
		