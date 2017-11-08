#!/usr/bin/env python3
import readline
import sys
from termcolor import colored, cprint

def add(arg1, arg2):
	return arg1 + arg2

def subtract(arg1, arg2):
	return arg1 - arg2

def multiply(arg1, arg2):
	return arg1 * arg2

def divide(arg1, arg2):
	return arg1 / arg2

ops = {
	'+': add,
	'-': subtract,
	'*': multiply,
	'/': divide    } 

def calculate(arg):
	# type 'q', then quit rpn program
	if arg == 'q':
		exit()
	# initialize stack
	stack = list()

	# perform calculations based on user input
	for token in arg.split():
		try:
			stack.append(int(token))
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = ops[token]
			result = function(arg1, arg2)
			stack.append(result)
	
	# print user input and color operators blue
	for token in arg:
		try:
			print(int(token), end="")
		except ValueError:
			cprint(token, 'blue', attrs=['bold'], end="")
	
	# printing result
	result = stack.pop()
	cprint(" = ", 'yellow', attrs=['bold'], end="")
	print(result)
	
	return result
	
def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()

