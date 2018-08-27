#!/bin/python

def answer(numbers):
    visited_pirates = []
    current_pirate = 0
    looping = False
    while True:
        next_pirate = numbers[current_pirate]
        if next_pirate in visited_pirates:
            if looping == False:
                looping = True
                visited_pirates = []
            else:
                return len(visited_pirates)
        else:
			visited_pirates.append(next_pirate)
			current_pirate = next_pirate