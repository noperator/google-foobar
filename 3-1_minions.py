#!/bin/env python

def answer(minions):

	###
	# Concise one-liner:
	###

	return sorted(range(len(minions)), key=lambda k: minions[k][0] * (float(minions[k][2]) / float(minions[k][1])))

	###
	# Human-friendly solution:
	###

	# # store minions length for multiple uses
	# len_minions = len(minions)

	# # list to store 
	# ranked_minions = [0]*len_minions

	# for i in range(len(minions)):
	# 	minion 			  = minions[i]
	# 	time 			  = minion[0]
	# 	probability 	  = float(minion[1]) / float(minion[2])
	# 	rank 			  = time / probability
	# 	ranked_minions[i] = rank

	# return sorted(range(len_minions), key=lambda k: ranked_minions[k])