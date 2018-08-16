def answer(ws):


	# transitive closure algorithm implementation, borrowed from soulcheck
	def transitive_closure(a):
		closure = set(a)
		while True:
			new_relations = set((x,w) for x,y in closure for q,w in closure if q == y)
			closure_until_now = closure | new_relations
			if closure_until_now == closure:
				break
			closure = closure_until_now
		return closure


	# comparator which uses rules, derived below, to sort alphabet
	def before(a, b):
		for rule in rules_closed:
			if a in rule and b in rule:
				if rule.index(a) > rule.index(b):
					return 1
				else:
					return -1


	# list to store derived relationships between letters
	rules = []
	
	# for each index, ending with the last index of the longest word
	for i in range(len(max(ws, key=len))):

		# retrieve each word indexable at the current index 'i' (read: 'indexable word')
		iws = [w for w in ws if len(w) >= i+1]
		
		# for each indexable word, 'w'
		for j,w in enumerate(iws):

			# retrieve all indexable words preceding 'w' in the dicitonary,
			# where each word is identical to 'w', save the character at index 'i'
			pws = [pw for pw in iws[:j] if pw[:i] == w[:i] and pw[i] != w[i]]

			# since these words have identical preceding substrings ':i',
			# lexicographical ordering has been deferred to the characters at 'i';
			# therefore, store this order
			rules += [(pw[i], w[i]) for pw in pws]

	# retrieve all unique letters in alphabet
	alphabet = list(set(''.join(ws)))

	# transitively close the derived rules
	rules_closed = transitive_closure(rules)

	# return alphabet, ordered according to closed rules
	return ''.join(sorted(alphabet, cmp=before))
