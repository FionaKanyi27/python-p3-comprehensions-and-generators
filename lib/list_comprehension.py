#!/usr/bin/env python3

def return_evens(num_list):
    """
    Returns a list of even numbers from the input list.

    Parameters:
    num_list (list of int): A list of integers.

    Returns:
    list of int: A list containing only even numbers from num_list.
    """
    return [n for n in num_list if n % 2 == 0]

def make_exclamation(sentence_list):
    pass