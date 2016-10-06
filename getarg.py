# Getarg is a Python module for quickly and easily finding the value of command like arguments if supplied.
# System Info:
# Version: 1.0.0 Stable
# Date: 10/01/2016
# Author: Kyle Piira
# Copyright 2016 Hoxly, Inc.

# Imports
import sys

# Functions
def get(arg):
	argument_recieved = False
	for argument in sys.argv[1:]:
		argument = argument.split('=')
		if argument[0] == arg:
			return argument[1]
			argument_recieved = True
	if argument_recieved == False:
		return False
def getposition(pos):
	try:
		return sys.argv[pos].split('=')
	except IndexError:
		return 'Error'