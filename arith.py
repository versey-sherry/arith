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
        result = ""
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
    			value = self.num()
    			return Token("INTEGER", value)
    		
    		if self.current_char == "+":
    			self.next()
    			return Token("PLUS", "+")

    		if self.current_char == "-":
    			self.next()
    			return Token("MINUS", "-")

    		if self.current_char == "*":
    			self.next()
    			return Token("MUL", "*")

#Parser
#Parse the tokens into an AST
class Paser():
	def __init__(self, text):
		self.text = text


#Interpreter
#Evaluate the programing with AST

def main():
	while True:
		try:
			#Taking raw inputs
			text = input()
		except EOFError:
			break

