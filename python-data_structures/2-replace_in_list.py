#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
	"""Replaces an element of a list at a specific position.

	Args:
		my_list (list): The list to modify.
		idx (int): The index of the element to replace.
		element (any): The new element to insert.
	"""
	if idx < 0 or idx >= len(my_list):
		return my_list
	my_list[idx] = element
	return my_list