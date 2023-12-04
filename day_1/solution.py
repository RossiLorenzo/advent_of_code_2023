# Libraries
import re

# Utility function to find first and last digit
def find_first_and_last_digit(my_string):
	all_digits = re.findall(r'\d', my_string)
	return int(all_digits[0] + all_digits[-1])

# Solution 1
def solution_1(input):
	s = 0
	for i in input:
		s = s + find_first_and_last_digit(i)
	return(s)

def replace_numbers(my_string):
	numbers_text = {
		'one': '1', 'two': '2', 'three': '3', 'four': '4', 
		'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
	}

	# Find the first number from left to right and right to left
	for pattern, value in numbers_text.items(): 
		if pattern in my_string:
			my_string = my_string.replace(pattern, pattern + value + pattern)
	
	return my_string

# Solution 2
def solution_2(input):
	s_u = []
	for s in input:
		s_u.append(replace_numbers(s))
	return(solution_1(s_u))

# Main
def main():
	# Import file input_part_1.txt
	input_file = open('input_part_1.txt', 'r')
	input_lines = input_file.readlines()
	
	# Solution 1
	print('Solution 1: ' + str(solution_1(input_lines)))

	# Solution 2
	print('Solution 2: ' + str(solution_2(input_lines)))

main()