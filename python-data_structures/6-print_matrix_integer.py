#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	"""Print a matrix of integers.

	Args:
		matrix (list of list of int): The matrix to print.
	"""
	for row in matrix:
		for i in range(len(row)):
			if i != len(row) - 1:
				print("{:d} ".format(row[i]), end="")
			else:
				print("{:d}".format(row[i]))