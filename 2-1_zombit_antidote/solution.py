def answer(requests): # renamed meetings to requests, for clarity
	
	# uniquify and sort requests
	requests = [list(x) for x in set(tuple(x) for x in requests)]
	requests = sorted(requests, key = lambda x: (int(x[0]), int(x[1])))
	
	# store recursively-generated meeting combinations
	# initialized with base case
	meeting_combinations = [[[0,0]]]

	# provide each accepted meeting request with a ranking
	rankings = [0] * len(requests)

	# recursively generate combinations of accepted meeting requests
	def check(list_num, meet_num, req_num):

		# prevent out-of-bounds indexing
		if req_num == len(requests):
			return

		# initialize iteration variables
		next_request = requests[req_num]
		last_meeting = meeting_combinations[list_num][meet_num]

		# can the next meeting request fit after the last accepted meeting?
		if next_request[0] >= last_meeting[1]:
			
			# if so, has another check() call already accepted this meeting?
			if rankings[req_num] > len(meeting_combinations[list_num])+1:
				
				# if so, exit to avoid duplicate effort
				return
			
			# otherwise, accept this meeting...
			meeting_combinations[list_num].append(next_request)
			
			# ...record the ranking...
			rankings[req_num] = len(meeting_combinations[list_num])
			
			# ...and check for more meetings!
			check(list_num, meet_num+1, req_num+1)

		# if not, would an earlier meeting be compatible with the request?
		else:

			# record the current combination, minus the most recent meeting
			current_list = meeting_combinations[list_num][:-1]

			# first, continue with current list of accepted meetings
			check(list_num, meet_num, req_num+1)

			# second, fork and create a new list to try the meeting request
			meeting_combinations.append(current_list)
			check(len(meeting_combinations)-1, meet_num-1, req_num)


	# check for meeting combinations!
	check(0, 0, 0)

	# return the longest list (decremented to account for base case)
	return  len(max(meeting_combinations,key=len))-1
