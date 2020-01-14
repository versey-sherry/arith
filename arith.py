#Lexer
#Tokenize the inputs
#Token type PLUS MUL MINUS INTEGER
class Token():
	def __init__(self, type, value):
		self.type = type
		self.value = value
	#String representation for debugging just in case
	def __repr__(self):
		return 'Token({type},{value})'.format(type = self.type, value = repr(self.value))
#lexer
class Lexer():
	def__init__(self, text):
	self.text = text
	#Start from the first character
	self.pos = 0
	self.current_char = self.text[self.pos]

	def error(self):
		raise Exception("Invalid inputs")

	#advance to the next character
	def next(self):
		self.pos +=1
		if self.pos > len(text) -1:
			self.current_char = None
		else:
			self.current_char = self.text[self.pos]

	#skipping white spaces
	def skipwhitespace(self):
		while self.current_char is not None and self.current_char.isspace():
			self.next()

	#multiple digits
	def num(self):
		result = ""
		while self.current_char is not None and self.current_char.indigit():
			result = rusult + self.current_char
		return int(result)
#Parser
#Parse the tokens into an AST

#Interpreter
#Evaluate the programing with AST

def main():
	while True:
		try:
			#Taking raw inputs
			text = input()
		except EOFError:
			break

