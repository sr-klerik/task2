#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from sys import argv

#Организация работы стека
class Stack:

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def is_empty(self):
		return (self.items == [])


#Основной класс генератора html из входного файла с выводом в другой файл
class GeneratorHTML:

	def __init__(self,input_file,output_file):
		try:
			self.input_file=open(input_file,"r")
			self.output_file=open(output_file,"w")
			self.stack = Stack()
		except IOError:
			print "Файл не найден"

	#Метод записи открытого тега по ключевому слову
	def print_open_teg(self,teg):
		return "%s<%s>\n" % ("\t"*(teg.count("\t")),teg.strip())

	#Метод записи закрытого тега по ключевому слову
	def print_closed_teg(self,teg):
		return "%s</%s>\n" % ("\t"*(teg.count("\t")),teg.strip())

	#Метод генерации html тегов по входным данным
	def create_html(self):
		for line in self.input_file:
			if self.stack.is_empty():
				if line:
					self.output_file.write(self.print_open_teg(line))
					self.stack.push(line)
			else:
				if line.count("\t") > last_teg.count("\t"):
					self.output_file.write(self.print_open_teg(line))
					self.stack.push(line)
				elif line.count("\t") <= last_teg.count("\t"):
					while self.stack.items[-1].count("\t") >= line.count("\t") and not self.stack.is_empty():
						self.output_file.write(self.print_closed_teg(self.stack.pop()))
					self.output_file.write(self.print_open_teg(line))
					self.stack.push(line)
			last_teg = line
		while not self.stack.is_empty():
			self.output_file.write(self.print_closed_teg(self.stack.pop()))

#Описание аргументов для запуска программы
parser = argparse.ArgumentParser(conflict_handler='resolve',description="""Программа для генерирования тегов html из файла. 
	Во входном файле указываются названия тегов	и отступы в соотвествии с вложенностью тегов. Теги указываются именами без кавычек и скобок
	, например: title. Указания отступа выполняются табуляцией.""", epilog = '''(c)Dmitry Makarov 2015''')
parser.add_argument('-i','--input_file',action='store', help="Входной файл из которого извлекает данные генератор html.")
parser.add_argument('-o','--output_file',action='store', help="Выходной файл.")
result=parser.parse_args()

if len(argv) != 5:
	parser.print_help()
else:
	try:
		gener = GeneratorHTML(result.input_file,result.output_file)
		gener.create_html()
	except IndexError:
		print "Неверно составлен входной файл"
	except IOError:
		print "Входного файла с таким именем не найдено"