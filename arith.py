#I mainly followed this post https://ruslanspivak.com/lsbasi-part7/

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
	def __init__(self, text):
		self.text = text
		#Start from the first character
		self.pos = 0
		self.current_char = self.text[self.pos]

	def error(self):
		raise Exception("Invalid inputs")

	#advance to the next character
	def next(self):
		self.pos +=1
		if self.pos > len(self.text) -1:
			self.current_char = None
		else:
			self.current_char = self.text[self.pos]

	#skipping white spaces
	def skipwhitespace(self):
		while self.current_char is not None and self.current_char.isspace():
			self.next()

	#multiple digits
	def num(self):
		result = ''
		while self.current_char is not None and self.current_char.isdigit():
			result = result + self.current_char
			self.next()

		return int(result)

	#return lexical token one at a time
	def tokenize(self):
		#nicer than elif, return breaks the loop
		while self.current_char is not None:
	
			if self.current_char.isspace():
				self.next()

			if self.current_char.isdigit():
				return Token("INTEGER", self.num())

			if self.current_char == "+":
				self.next()
				return Token("PLUS", "+")

			if self.current_char == "-":
				self.next()
				return Token("MINUS", "-")

			if self.current_char == "*":
				self.next()
				return Token("MUL", "*")

			self.error()

		return(Token("EOF", None))

#Parser
#Parse the tokens into an AST
class AST():
	pass

class PlusNode():
	#some value from term
	#some value form expression
	def __init__(self, left, right):
		self.left = left
		self.right = right
		self.op = "PLUS"

class MinusNode():
	#some value from term
	#some value form expression
	def __init__(self, left, right):
		self.left = left
		self.right = right
		self.op = "MINUS"

class MulNode():
	#some factor
	#some value from term
	def __init__(self, left, right):
		self.left = left
		self.right = right
		self.op = "MUL"

#For positive negative integers, operations that only happen to the one token after it
class OnaryNode():
	def __init__(self, token):
		pass

#A node for all the integers
class IntNode():
	def __init__(self, token):
		self.token = token
		self.value = self.token.value

class Parser():
	def __init__(self, lexer):
		#initially the pos is at 0. self.current_token returns the token for the current char
		#tokenize also move pos to the next one and record the next char for lexer.
		self.lexer = lexer
		self.current_token = self.lexer.tokenize()

	def error():
		raise error("Invalid syntax.")

	#Only evaluate integers and create num node
	def factor(self):
		token = self.current_token
		if token.type == "INTEGER":
			node = IntNode(token)
			self.current_token = self.lexer.tokenize()
			return node

	#Only evaluate multiplication and create mul node
	def term(self):
		node = self.factor()
		token = self.current_token
		if token.type == "MUL":
			self.current_token = self.lexer.tokenize()
			node = MulNode(left = node, right = self.factor())
			return node


	#Evaluate plus and minus and create nodes
	def expr(self):
		node = self.term()
		token = self.current_token 
		if token.type = "PLUS":
			self.current_token = self.lexer.tokenize()
			node = PlusNode(left = node, right = self.term())
		elif token.type = "MINUS":
			node = MinusNode(left = node, right = self.term())
		return node

	def parse(self):
		return self.expr()

#Interpreter
#Evaluate the programing with AST

def main():
	while True:
		try:
			#Taking raw inputs
			text = input()
		except EOFError:
			break

