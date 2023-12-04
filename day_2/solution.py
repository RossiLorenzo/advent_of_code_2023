import re

# Solution 1: games possible with 12 red cubes, 13 green cubes, and 14 blue cubes
def solution_1(input, m = [12, 13, 14]):
	s = 0
	for i in input:
		max_c = []
		for c in ['red', 'green', 'blue']:
			max_c.append(max(i['blocks'][c]))

		if max_c[0] <= m[0] and max_c[1] <= m[1] and max_c[2] <= m[2]:
			s = s + i['gameid']
	return(s)

# Solution 2: minum cubes per game
def solution_2(input):
	s = 0
	for i in input:
		max_c = []
		for c in ['red', 'green', 'blue']:
			max_c.append(max(i['blocks'][c]))

		s = s + max_c[0] * max_c[1] * max_c[2]
	return(s)

# Main
def main():
	# Import file input_part_1.txt
	input_file = open('input_part_1.txt', 'r')
	input_lines = input_file.readlines()

	# Split each line in a dictionary
	input_lines_clean = []
	for l in input_lines:
		# Split on ;
		l_s = l.split(';')
		# For each split find green, blue, red (coalescing to 0)
		blocks = {'red': [], 'green': [], 'blue': []}
		for s in l_s:
			for c in ['red', 'green', 'blue']:
				m = re.search('(\d*) ' + c, s)
				if m:
					blocks[c].append(int(m.group(1)))
				else:
					blocks[c].append(0)
		# Return clean dictionaries
		input_lines_clean.append({
			'gameid': int(re.search('Game (\d*)', l).group(1)),
			'blocks': blocks	
		})

	# Solution 1
	print('Solution 1: ' + str(solution_1(input_lines_clean)))

	# Solution 2
	print('Solution 2: ' + str(solution_2(input_lines_clean)))

main()