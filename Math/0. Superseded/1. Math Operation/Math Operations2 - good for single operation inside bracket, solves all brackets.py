#2020-10-26
#given a string with a math equation, program performs the operations in the proper operation

import re

def FindMultiInstances(str1, character):
	list_idx = []
	for idx, item in enumerate(str1):
		if item == character:
			list_idx.append(idx)
	print(f'There are {len(list_idx)} instances of character "{character}"')
	print(list_idx)
	return list_idx

def BracketIdxs(str1):
	list_idxStart, list_idxranges = [],[]
	for idx,item in enumerate(str1):
		if (item == '(') | (item == "["):
			list_idxStart.append(idx)		
		if (item == ')') | (item == "]"):
			list_idxranges.append(f'{list_idxStart[-1]}:{idx}')
			list_idxStart.pop()
	print(list_idxStart, list_idxranges)

	for entry in list_idxranges:
		idx_low = int(entry.split(':')[0])+1
		idx_high = int(entry.split(':')[1])
		print(str1[idx_low:idx_high])

# str1 = '[(3+(22/2))/(3+9)]'
# BracketIdxs(str1)






class Math():
	def __init__(self, math_str):
		self.eqn = math_str
		self.completion = False

	def BracketIdxs(self):
		list_idxStart, list_idxranges = [],[]
		for idx,item in enumerate(self.eqn):
			if (item == '(') | (item == "["):
				list_idxStart.append(idx)		
			if (item == ')') | (item == "]"):
				list_idxranges.append(f'{list_idxStart[-1]}:{idx}')
				list_idxStart.pop()
		# print(list_idxStart, list_idxranges)

		#this reviews the various bracket operations that must be executed
		for idx, entry in enumerate(list_idxranges):
			idx_low = int(entry.split(':')[0])+1
			idx_high = int(entry.split(':')[1])
			# print(self.eqn[idx_low:idx_high])

			#the first entry is the first bracket that must be solved
			if idx ==0:
				str_mathfirst=self.eqn[idx_low:idx_high]
				idx0_low=idx_low
				idx0_high=idx_high


		if len(list_idxranges)==1:
			self.completion = True

		return str_mathfirst, idx0_low, idx0_high, self.completion

	def MathOperations(self, eqn_InBracket, idx0_low, idx0_high):

		#get list of all the numbers in equation
		list_eqn_splitUp = re.split('[+-/*]',eqn_InBracket)
		list_eqn_splitUp = [int(x) for x in list_eqn_splitUp]
		print(list_eqn_splitUp)

		#get list of the math operations
		list_idxs, list_operators =[],[]
		list_mathOperators = '+ - * /'
		idx=0
		for character in eqn_InBracket:
			if character in list_mathOperators:
				# print(character)
				list_operators.append(character)
		print(list_operators)


		#perform the exponential
		print(f'*****Executing all EXPONENTIAL entries{"_"*50}')
		while True:
			try:
				idx_div = list_operators.index('^')
				# print(idx_div)

				print(list_eqn_splitUp)

				num_i = list_eqn_splitUp[idx_div]^list_eqn_splitUp[idx_div+1]
				list_eqn_splitUp[idx_div]=num_i
				del list_eqn_splitUp[idx_div+1]
				del list_operators[idx_div]
				print(list_eqn_splitUp)
				print(list_operators)
			except:
				print('end of Exponential')
				break


		#perform the multiplification
		print(f'*****Executing all MULTIPLIFICATION entries{"_"*50}')
		while True:
			try:
				idx_div = list_operators.index('*')
				# print(idx_div)

				print(list_eqn_splitUp)

				num_i = list_eqn_splitUp[idx_div]*list_eqn_splitUp[idx_div+1]
				list_eqn_splitUp[idx_div]=num_i
				del list_eqn_splitUp[idx_div+1]
				del list_operators[idx_div]
				print(list_eqn_splitUp)
				print(list_operators)
			except:
				print('end of Multiplification')
				break

		#perform the division
		print(f'*****Executing all DIVISION entries{"_"*50}')
		while True:
			try:
				idx_div = list_operators.index('/')
				# print(idx_div)

				print(list_eqn_splitUp)

				num_i = list_eqn_splitUp[idx_div]/list_eqn_splitUp[idx_div+1]
				list_eqn_splitUp[idx_div]=num_i
				del list_eqn_splitUp[idx_div+1]
				del list_operators[idx_div]
				print(list_eqn_splitUp)
				print(list_operators)
			except:
				print('end of Division')
				break

		#perform the addition
		print(f'*****Executing all ADDITION entries{"_"*50}')
		while True:
			try:
				idx_div = list_operators.index('+')
				# print(idx_div)

				print(list_eqn_splitUp)

				num_i = list_eqn_splitUp[idx_div]+list_eqn_splitUp[idx_div+1]
				list_eqn_splitUp[idx_div]=num_i
				del list_eqn_splitUp[idx_div+1]
				del list_operators[idx_div]
				print(list_eqn_splitUp)
				print(list_operators)
			except:
				print('end of Addition')
				break

		#perform the subtraction
		print(f'*****Executing all SUBTRACTION entries{"_"*50}')
		while True:
			try:
				idx_div = list_operators.index('+')
				# print(idx_div)

				print(list_eqn_splitUp)

				num_i = list_eqn_splitUp[idx_div]-list_eqn_splitUp[idx_div+1]
				list_eqn_splitUp[idx_div]=num_i
				del list_eqn_splitUp[idx_div+1]
				del list_operators[idx_div]
				print(list_eqn_splitUp)
				print(list_operators)
			except:
				print('end of Subtraction')
				break

		original_str = self.eqn
		if idx0_low!=0:
			idx0_low-=1
		if idx0_high != len(self.eqn)-1:
			idx0_high+=1

		new_str = self.eqn[0:idx0_low]+f"{list_eqn_splitUp[0]}"+self.eqn[idx0_high:]
		print(f'\t {"_"*25}Updated equation string: "  {new_str}  "')
		self.eqn = new_str
		return list_eqn_splitUp[0]



	def InsideBracket(self):
		print('\t__InsideBracket Function____')
		print(self.eqn)

		#test if multiple brackets 
		MultiBracks = FindMultiInstances(self.eqn, '(')

		Bracket_i = self.eqn.find('(')
		Bracket_j = self.eqn.find(')')
		math_in_bracket = self.eqn[Bracket_i:Bracket_j+1].replace('(','').replace(')','')
		print(math_in_bracket)
		return math_in_bracket




def main():
	str_math = r"25*(312+(22/2))^2-38"
	calc = Math(str_math)
	break_loop = 0
	while True:
		print('\n\n')
		if break_loop>2:
			break
		calc_i,idx0_low,idx0_high,completion = calc.BracketIdxs()
		print(calc_i, idx0_low, idx0_high)
		print(str_math[idx0_low-1:idx0_high+1])
		num_i = calc.MathOperations(calc_i, idx0_low,idx0_high)
		if completion == True:
			print('***No more brackets!')
			break
		
		
		break_loop+=1

	# math_in_bracket = calc.InsideBracket()
	# num = calc.MathOperations(math_in_bracket)
	# print(num)

main()













