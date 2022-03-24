#2020-10-30
#reverse an equation

import re

def InBrackets(RHS, child_var, list_mathOperations, dict_bracketEqns):
	idx0=RHS.index(child_var)
	# print(idx0)
	print(f'RHS being review:: {RHS}')
	
	InBracketTest=False
	idx_test=idx0
	print(f'Initial idx_test:: {idx_test}')
	idx_LeftMathOperator=0
	while idx_test>=0:

		if RHS[idx_test] in list_mathOperations:
			idx_LeftMathOperator = idx_test

		if RHS[idx_test]=='(':
			left_idx=idx_test+1
			# print(f'left_idx == {left_idx}  VS idx_LeftMathOperator == {idx_LeftMathOperator}')
			# if left_idx > idx_LeftMathOperator:
			# 	InBracketTest = True
			InBracketTest = True
			break		
		# if RHS[idx_test] in list_mathOperations:
		# 	# left_idx=idx_test+1
		# 	break
		# print(RHS[idx_test])
		idx_test-=1
		print(f'Updated idx_Test for "(":: {idx_test}')

	if InBracketTest ==False:
		return RHS, dict_bracketEqns, InBracketTest 
	# print(f'left_idx:: {left_idx}')

	# print(idx0)
	idx_test=idx0
	# print(f'length of RHS:: {len(RHS)}')
	# print(RHS[8])
	while (InBracketTest) & (idx_test<len(RHS)):
		if RHS[idx_test]==')':
			right_idx=idx_test		
			break
		# print(RHS[idx_test])
		idx_test+=1
		# print(f'Updated idx_Test for ")":: {idx_test}')

	bracket_terms0 = RHS[left_idx:right_idx]
	print(f'bracket_terms0=={bracket_terms0}')
	if ')' in bracket_terms0:
		InBracketTest = False
		return RHS, dict_bracketEqns, InBracketTest
	# print(f'bracket_terms is {bracket_terms}')
	# print(f'keys of dict is {dict_bracketEqns.keys()}')

	bracket_terms = RHS[left_idx-1:right_idx+1]
	if len(dict_bracketEqns.keys())==0:
		# print(f'dict_bracketEqns == {dict_bracketEqns}')
		# new_var = 'a'
		new_var = 'sub1'
		dict_bracketEqns[new_var]=bracket_terms
		RHS = RHS.replace(bracket_terms,new_var)

	else:
		max_var = max(dict_bracketEqns.keys())
		# new_var = chr(ord(max_var)+1)
		max_varNum =int(''.join(re.findall(r"\d", max_var)))
		# print(f'max_varNum=={max_varNum}')
		new_var = 'sub'+ str(max_varNum+1)
		dict_bracketEqns[new_var]=bracket_terms
		RHS = RHS.replace(bracket_terms,new_var)

	return RHS, dict_bracketEqns, InBracketTest



def ReverseEqn(str1, dict_reverse, child_var, list_mathOperations):
	LHS=str1.split('=')[0]
	RHS=str1.split('=')[1]
	# print(LHS, RHS)


	if len(re.findall(child_var, str1)) >1:
		reverse_eqn = f'More than one instance of the child_var "{child_var}" from the equation: "{str1}". ***This script is not setup for this.***'
		return reverse_eqn

	#Substitute all equations INSIDE OF BRACKETS with a term subi where i denotes the number of substitutions_______________________________________________________
	print(f'{">"*50} Subsitute terms with BRACKETS around the key child_var')
	dict_bracketEqns={}
	InBracketTest = True
	testnum = 1
	print(f'\n{"*"*5}Check # {testnum}:')
	RHS_i, dict_bracketEqns,InBracketTest = InBrackets(RHS, child_var, list_mathOperations, dict_bracketEqns)
	
	print(f'for Check # {testnum}, RHS_i== {RHS_i}')
	testnum+=1
	if len(dict_bracketEqns) != 0:
		child_var_i = max(dict_bracketEqns.keys())
		while InBracketTest == True:
			print(f'\n{"*"*5}Check # {testnum}:')
			RHS_i, dict_bracketEqns,InBracketTest = InBrackets(RHS_i, child_var_i, list_mathOperations, dict_bracketEqns)
			child_var_i = max(dict_bracketEqns.keys())
			print(f'for Check # {testnum}, RHS_i== {RHS_i}')
			# print(f'\nStep - Var inside bracket) \nRHS: {RHS} \ndict_bracketEqns: {dict_bracketEqns} \nInBracketsTest: {InBracketTest}')
			testnum+=1
			# if testnum>10:
			# 	break

	print(f'\n\nOriginal RHS string is: {RHS}')
	print(f'After check {testnum} for brackets, resulting string is: \nRHS_i: {RHS_i} \ndict_bracketEqns: {dict_bracketEqns} \nInBracketsTest: {InBracketTest}\n\n')
	#now the string has been filtered to exclude brackets in the equation string



def main():
	str1 = r'y=(w,n+2)-1*w,n'
	str1 = r'y=(w,n+2)-1'
	str1 = r'y=(2*(w,n+2))^2-1'
	str1 = r'y=(2*(w,n+2))^(2*3)-1'
	str1 = r'y=(2*(w,n+2))^(2*3)-((3*6)+2)+(3/2)'
	str1 = r'y=32*(2*(w,n+2))^(2*3)-((3*6)+2)'
	str1 = r'y=((3*6)+2)-32*(2*(w,n+2))^(2*3)*5'
	dict_reverse={'+':'-','-':'+'}
	list_mathOperations = '+ - / * ^ ='.split()
	child_var = 'w,n'
	reverse_eqn = ReverseEqn(str1, dict_reverse, child_var, list_mathOperations)
	# print(reverse_eqn)
main()




