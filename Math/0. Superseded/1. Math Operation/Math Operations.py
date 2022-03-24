#2020-10-26
#given a string with a math equation, program performs the operations in the proper operation

import re

class Math():
	def __init__(self, math_str):
		self.eqn = math_str
		pass

	def Multiply(self, eqn_InBracket):
		list_eqn_splitUp = re.split('[+-/*]',eqn_InBracket)
		print(list_eqn_splitUp)

		list_idxs =[]
		list_mathOperators = []
		idx=0

		for part in list_eqn_splitUp:
			print(f'part is {part}')
			idx_i = eqn_InBracket.find(part)
			# print(idx_i)
			list_idxs.append(f"{idx_i}:{idx_i+len(list_eqn_splitUp[0])}")
			list_mathOperators.append(idx_i+len(list_eqn_splitUp[0]))
			idx+=1
		
		print(list_idxs)
		print(list_mathOperators)

		for operator_idx in list_mathOperators:
			print(eqn_InBracket[operator_idx])


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

main()













