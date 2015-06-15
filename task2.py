#!/usr/bin/python

class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def is_empty(self):
		return (self.items == [])


class GeneratorHTML:
	def __init__(self,input_file,output_file):
		self.input_file=open(input_file,"r")
		self.output_file=open(output_file,"w")
		self.stack = Stack()


	def print_open_teg(self,teg):
		return "%s<%s>\n" % ("\t"*(teg.count("\t")),teg.strip())


	def print_closed_teg(self,teg):
		return "%s</%s>\n" % ("\t"*(teg.count("\t")),teg.strip())


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


gener = GeneratorHTML("./test.txt","./test2.txt")
gener.create_html()