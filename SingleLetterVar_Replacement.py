

def ReplaceSingleVar(str1, var_i, Replacement):
	new_str =''
	for idx, character in enumerate(str1):
		# print(character)
		if idx < len(str1)-1:
			if (character == var_i) & ((str1[idx+1].isalpha()) or (str1[idx+1]==',')):
				# print(character, idx)
				new_str+=character
			elif character == var_i:
				new_str+=Replacement
			else:
				new_str+=character
		else:
			if (character == var_i):
				new_str+=Replacement
			else:
				new_str+=character
			# print('reached last character')
	print(new_str)

	return new_str


def main():
	str1 = r'cost = c*center+c+c,2'
	var_i = 'c'
	# var_i= 'c,2'
	# dict_vars = {'c':'4', 'c,2':2}
	Replacement = '4'
	new_str = ReplaceSingleVar(str1, var_i, Replacement)

main()