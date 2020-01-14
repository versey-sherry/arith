# arith
Course Homework for Programming Languages. Implementing ARITH in Python

As per the homework requirement, this script will do the following things:
1. The script gets inputs via stdin and output via stdout
2. The script parses the input into an Abstract Syntax Tree (AST)
3. The AST is evaulated in the interpreter and the script outputs the results.

arith has three features, addition, multiplication and subtraction. Operations are applied to integers.

### Requirements:
python3 >=3.6

### Grammar
The grammar in the homework is
```
<expr> ::== <int>
           |<expr> + <expr>
           |<expr> * <expr>
```
However, to capture the order of predence, my grammar is
```
<expr> ::== <trm>
          | <expr> + <trm>
          | <expr> - <trm>
<trm> ::== <fac>
          |<trm> * <fac>
<fac> ::== <int>
```  
The AST is generated with this grammar.

### Reference:
Coming from not really knowing how interpreters work and needing to finish the homework within a week, here are the links I went over to get familiar with the topic:
1. Grammar, Syntax and Semantics: https://opendsa-server.cs.vt.edu/ODSA/Books/PL/html/index.html
2. Explanation of the concept: https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df
3. Tutorial for Python implementation: https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df
