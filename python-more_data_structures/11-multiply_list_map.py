#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
	"""Multiplies all elements of a list by a number using map.

	Args:
		my_list (list): A list of integers.
		number (int): The number to multiply each element by.

	Returns:
		list: A new list with all elements multiplied by the number.
	"""
	return list(map(lambda x: x * number, my_list))