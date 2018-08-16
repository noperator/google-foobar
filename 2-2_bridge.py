#!/bin/env python

def answer(x):

	return len(x) - ((sum(x) % len(x)) > 0)

	# Alternative human-friendly solution:
	# num_cars = len(x)
	# total_rabbits = sum(x)
	# remaining_rabbits = total_rabbits % num_cars
	# if remaining_rabbits == 0:
	#     return num_cars
	# else:
	#     return num_cars - 1