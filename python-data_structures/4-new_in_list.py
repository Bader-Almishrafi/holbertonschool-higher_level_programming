#!/usr/bin/python3
def new_in_list(my_list, idx, element):
	"""Replaces an element in a list at a specific position
	while leaving the original list unmodified.

	Args:
		my_list (list): The original list.
		idx (int): The index of the element to replace.
		element (any): The new element to insert.

	Returns:
		list: A new list with the modified element.
	"""
	if idx < 0 or idx >= len(my_list):
		return my_list.copy()
	new_list = my_list.copy()
	new_list[idx] = element
	return new_list