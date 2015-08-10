# -*- coding: utf8 -*-
import re


re_yes = re.compile('^y(?:es|eah)|si(?:mon)?|por supuesto$')
re_no  = re.compile('^n(?:op?|el)?|ni mergas|nones$')

def start_quiz():
	num = raw_input("¿te gustan los números?\nyo: ")
	if num is None:
		return "ni idea qué puedas estudiar"

	if re_yes.match(num):
		return "estudia matemáticas"

	return "no tengo idea"
