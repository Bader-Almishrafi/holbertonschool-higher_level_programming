#!/usr/bin/python3
def divisible_by_2(my_list=[]):
	"""Find all multiples of 2 in a list.

	Args:
		my_list (list): List of integers.

	Returns:
		list: List of booleans representing if the integer at that index is
		divisible by 2.
	"""
	return [num % 2 == 0 for num in my_list]