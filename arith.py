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
class Lexer():
	def__init__(self, text):
	self.text = text
	#Start from the first character
	self.pos = 0
	self.current_char = self.text[self.pos]

#Parser
#Parse the tokens into an AST

#Interpreter
#Evaluate the programing with AST
