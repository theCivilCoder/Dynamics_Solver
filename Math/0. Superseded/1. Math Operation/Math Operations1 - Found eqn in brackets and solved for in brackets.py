#2020-10-26
#given a string with a math equation, program performs the operations in the proper operation

import re

class Math():
	def __init__(self, math_str):
		self.eqn = math_str
		pass

	def Multiply(self, eqn_InBracket):

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

		return list_eqn_splitUp[0]



	def InsideBracket(self):
		Bracket_i = self.eqn.find('(')
		Bracket_j = self.eqn.find(')')
		math_in_bracket = self.eqn[Bracket_i:Bracket_j+1].replace('(','').replace(')','')
		print(math_in_bracket)
		return math_in_bracket




def main():
	str_math = r"25*(312+22/2)^2-38"
	calc = Math(str_math)
	math_in_bracket = calc.InsideBracket()
	num = calc.Multiply(math_in_bracket)
	print(num)

main()













