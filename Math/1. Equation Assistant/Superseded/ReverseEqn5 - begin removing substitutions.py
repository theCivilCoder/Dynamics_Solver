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
	while idx_test>=0:

		if RHS[idx_test]=='(':
			left_idx=idx_test+1
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

	bracket_terms = RHS[left_idx-1:right_idx+1]
	print(f'bracket_terms=={bracket_terms}')
	# print(f'bracket_terms is {bracket_terms}')
	# print(f'keys of dict is {dict_bracketEqns.keys()}')

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

def SubBrackets_NonKeyVar(RHS, list_mathOperations, dict_bracketEqns_NotKeyVar):
	InBracketTest=False
	idx_test=0
	while idx_test<len(RHS):
		if RHS[idx_test]=='(':
			left_idx=idx_test
			print(f'left_idx == {left_idx}')
			InBracketTest = True	
		if RHS[idx_test]==')':
			right_idx=idx_test
			print(f'right_idx == {right_idx}')
			break
		idx_test+=1

	if InBracketTest ==False:
		return RHS, dict_bracketEqns_NotKeyVar, InBracketTest 

	bracket_terms = RHS[left_idx:right_idx+1]
	print(f'bracket_terms=={bracket_terms}')
	# print(f'bracket_terms is {bracket_terms}')
	# print(f'keys of dict is {dict_bracketEqns_NotKeyVar.keys()}')

	if len(dict_bracketEqns_NotKeyVar.keys())==0:
		# print(f'dict_bracketEqns_NotKeyVar == {dict_bracketEqns_NotKeyVar}')
		# new_var = 'a'
		new_var = 'subNK1'
		dict_bracketEqns_NotKeyVar[new_var]=bracket_terms
		RHS = RHS.replace(bracket_terms,new_var)

	else:
		max_var = max(dict_bracketEqns_NotKeyVar.keys())
		# new_var = chr(ord(max_var)+1)
		max_varNum =int(''.join(re.findall(r"\d", max_var)))
		# print(f'max_varNum=={max_varNum}')
		new_var = 'subNK'+ str(max_varNum+1)
		dict_bracketEqns_NotKeyVar[new_var]=bracket_terms
		RHS = RHS.replace(bracket_terms,new_var)

	return RHS, dict_bracketEqns_NotKeyVar, InBracketTest	
	


def SubExpMultDiv(RHS, child_var, list_mathOperations, dict_bracketEqns):
	condition = False
	# print(idx0)
	print(f'RHS being reviewed:: {RHS}')
	# print(RHS, child_var, list_mathOperations, dict_bracketEqns)
	print(f'child_var:: {child_var}')
	print(f'dict_bracketEqns:: {dict_bracketEqns}')

	#get the list of variables/numbers
	new_var = ''
	list_variables=[]
	list_operators = []
	for character in RHS:
		# print(character)
		if character in list_mathOperations:
			list_variables.append(new_var)
			list_operators.append(character)
			new_var=''
			continue
		new_var+=character
	list_variables.append(new_var)
	print(list_variables)
	print(list_operators)
	# list_eqn_splitUp = re.findall(r'[+-]?\d*\.\d+|\d+',RHS)
	# print(list_eqn_splitUp)

	#create the new dict subsitution term here but only add it to the dictionary if an exponential, a multiplification or a division is found around the key term
	if len(dict_bracketEqns.keys())==0:
		new_var = 'sub1'
	else:
		max_var = max(dict_bracketEqns.keys())
		max_varNum =int(''.join(re.findall(r"\d", max_var)))
		new_var = 'sub'+ str(max_varNum+1)

	#identify and subsitute the exponential__________________________________________________________________________________
	if '^' in RHS:
		idx_exp = RHS.index(child_var)+len(child_var)+1 #beginning of new_var
		if RHS[idx_exp-1] == '^':
			# print(f'idx_exp == {idx_exp}')
			# print(f'{RHS[idx_exp]}')
			new_var_j=''
			while True:
				character = RHS[idx_exp]
				if character in list_mathOperations:
					break
				new_var_j+=character
				idx_exp+=1
			RHS = RHS.replace(f'{child_var}^{new_var_j}',new_var)
			dict_bracketEqns[new_var]= f'{child_var}^{new_var}'
			condition=True
			print(f'Found the exponential')
			return RHS, dict_bracketEqns, condition

	# print('check is passing earlier return')
	#identify and subsitute the multiplication___________________________________________________________________________
	if "*" in RHS:
		idx_expLEFT = RHS.index(child_var)-1
		if RHS[idx_expLEFT]=='*':
			print(f'RHS[idx_expLEFT] == {RHS[idx_expLEFT]}')
			idx_expLEFT-=1			
			new_var_j=''
			while True:
				character = RHS[idx_expLEFT]
				if (character in list_mathOperations) | (idx_expLEFT<0):
					break
				# if idx_expLEFT<0:
				# 	break
				new_var_j=character+new_var_j
				idx_expLEFT-=1
			print(f'new_var_j=={new_var_j}')
			print(RHS.replace(f'{new_var_j}*{child_var}',new_var))
			# RHS = RHS.replace(f'{child_var}*{new_var_j}',new_var)
			RHS = RHS.replace(f'{new_var_j}*{child_var}',new_var)
			dict_bracketEqns[new_var]= f'{new_var_j}*{child_var}'
			condition=True
			return RHS, dict_bracketEqns, condition		
	
		idx_expRIGHT = RHS.index(child_var)+len(child_var)
		print(f'RHS[idx_expRIGHT] == {RHS[idx_expRIGHT]}')
		if RHS[idx_expRIGHT]=='*':
			idx_expRIGHT+=1
			new_var_j=''
			print(f'RHS::: {RHS}')
			while True:			
				character = RHS[idx_expRIGHT]
				if (character in list_mathOperations) | (idx_expRIGHT==len(RHS)-1):
					break	
				new_var_j+=character
				idx_expRIGHT+=1
			# print(f'new_var=={new_var}')
			# print(f'{child_var}^{new_var_j}')
			print(f'for new_var== {new_var}, new_var_j == {new_var_j}')
			print(RHS.replace(f'{child_var}*{new_var_j}',new_var))
			RHS = RHS.replace(f'{child_var}*{new_var_j}',new_var)
			dict_bracketEqns[new_var]= f'{child_var}*{new_var_j}'
			condition=True
			# print(f'Found the exponential')
			return RHS, dict_bracketEqns, condition	

	#returns the original RHS, dict_bracketEqns, and condition=False if no exponentials, multipliciation or division is found
	return RHS, dict_bracketEqns, condition


def RevNK_AddSub(LHS, RHS_i, list_mathOperations, dict_bracketEqns, dict_bracketEqns_NotKeyVar, dict_reverse):
	LHS_i = LHS
	condition=False

	max_var = max(dict_bracketEqns.keys())
	print(max_var)

	#first deal with the addition/subtraction to the right of the max_var
	idx_maxVarRIGHT = RHS_i.index(max_var)+len(max_var)-1 #adding length makes idx_maxVarRIGHT so I subtract 1 to end at the end of the max_var

	if idx_maxVarRIGHT < len(RHS_i)-1:
		print(f'idx_maxVarRIGHT == {idx_maxVarRIGHT}  and len(RHS_i) == {len(RHS_i)}')
		idx_maxVarRIGHT+=1
		#if there is math happening to the right of the max_var
		MathOp = RHS_i[idx_maxVarRIGHT]
		print(MathOp)
		idx_maxVarRIGHT+=1
		#new_var/number immediately right of the max_var		
		new_var =''
		while True:
			character = RHS_i[idx_maxVarRIGHT]
			# print(character)
			if character in list_mathOperations:
				break
			idx_maxVarRIGHT+=1
			if idx_maxVarRIGHT==len(RHS_i):
				new_var+=character
				break
			new_var+=character
		print(f'new_var == {new_var}')

		RevMathOp = dict_reverse[MathOp]
		print(f'LHS = {LHS}{RevMathOp}{new_var}')
		LHS_i = f'{LHS}{RevMathOp}{new_var}'
		RHS_i = RHS_i.replace(f'{MathOp}{new_var}','')
		condition=True
		return LHS_i, RHS_i,condition

	#if there is no math to the right then proceed with the following code to reverse the math happening left of the max_var
	idx_maxVarLEFT = RHS_i.index(max_var)
	print(f'looking left:: {RHS_i[idx_maxVarLEFT]}')
	if idx_maxVarLEFT == 0:
		return LHS_i, RHS_i, condition
	idx_maxVarLEFT-=1
	mathOp = RHS_i[idx_maxVarLEFT]
	print(f'mathOp is "{mathOp}"')
	RevMathOp = dict_reverse[mathOp]
	# idx_maxVarLEFT-=1
	RHS_rest = RHS_i[0:idx_maxVarLEFT]
	if mathOp == '-':
		LHS_i = f'({RHS_rest})-({LHS_i})'
		RHS_i = RHS_i.replace(f'{RHS_rest}','').replace('-','')
	elif mathOp == '+':
		LHS_i = f'{LHS_i}{RevMathOp}({RHS_rest})'
		RHS_i = RHS_i.replace(f'{RHS_rest}','').replace('+','-')
	condition = True
	# idx_maxVarLEFT-=1
	# new_var=''
	# while True:
	# 	character = RHS_i[idx_maxVarLEFT]
	# 	if character in list_mathOperations:
	# 		if character == '-':
	# 			new_var = '-'+new_var
	# 		break
	# 	idx_maxVarLEFT-=1
	# 	if idx_maxVarLEFT <0:
	# 		new_var = character+new_var
	# 		break
	# 	new_var = character+new_var
	# print(f'new_var == {new_var}')

	return LHS_i, RHS_i, condition


def Loop_RevNK_AddSub(LHS, RHS_i, list_mathOperations, dict_bracketEqns, dict_bracketEqns_NotKeyVar, dict_reverse):
	#Begin reversing the math operations; beginning with adding/subtracting the NOT KEY TERMS
	print(f'\n\n{">"*50} Begin RERVERSING LHS and RHS starting with ADDING/SUBTRACTING THE NOT KEY TERMS')
	print(f'LHS:: {LHS}')
	print(f'RHS:: {RHS_i}')
	LHS_i = LHS
	testnum = 1
	print(f'\n{"*"*5}Check # {testnum}:')
	LHS_i, RHS_i, condition = RevNK_AddSub(LHS, RHS_i, list_mathOperations, dict_bracketEqns, dict_bracketEqns_NotKeyVar, dict_reverse)
	print(f'for Check # {testnum}, LHS_i=={LHS_i}   AND  RHS_i== {RHS_i}')
	testnum+=1
	while condition:
		print(f'\n{"*"*5}Check # {testnum}:')
		LHS_i, RHS_i, condition = RevNK_AddSub(LHS_i, RHS_i, list_mathOperations, dict_bracketEqns, dict_bracketEqns_NotKeyVar, dict_reverse)
		print(f'for Check # {testnum}, LHS_i=={LHS_i}   AND  RHS_i== {RHS_i}')
		if testnum>5:
			break
		testnum+=1
	return LHS_i, RHS_i


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

	#Substitute all equations INSIDE OF BRACKETS with a term subNKi where i denotes the number of substitutions around items that are NOT the KEY Variable_______________________________________________________
	print(f'{">"*50} Subsitute terms with BRACKETS around any terms that are NOT the KEY Variable')
	RHS_i_beforeBracketsNK = RHS_i
	dict_bracketEqns_NotKeyVar={}
	
	InBracketTest = True
	testnum = 1
	print(f'\n{"*"*5}Check # {testnum}:')
	RHS_i, dict_bracketEqns_NotKeyVar,InBracketTest =SubBrackets_NonKeyVar(RHS_i, list_mathOperations, dict_bracketEqns_NotKeyVar)
	print(f'for Check # {testnum}, RHS_i== {RHS_i}')
	testnum+=1	
	if len(dict_bracketEqns_NotKeyVar) != 0:
		# child_var_i = max(dict_bracketEqns_NotKeyVar.keys())
		while InBracketTest == True:
			print(f'\n{"*"*5}Check # {testnum}:')
			RHS_i, dict_bracketEqns_NotKeyVar,InBracketTest = SubBrackets_NonKeyVar(RHS_i, list_mathOperations, dict_bracketEqns_NotKeyVar)
			# child_var_i = max(dict_bracketEqns_NotKeyVar.keys())
			print(f'for Check # {testnum}, RHS_i== {RHS_i}')
			# print(f'\nStep - Var inside bracket) \nRHS: {RHS} \ndict_bracketEqns: {dict_bracketEqns} \nInBracketsTest: {InBracketTest}')
			testnum+=1
	print(f'\n\nOriginal RHS string before checking brackets NOT around KEY variable is: {RHS_i_beforeBracketsNK}')
	print(f'After check {testnum} for brackets, resulting string is: \nRHS_i: {RHS_i} \ndict_bracketEqns_NotKeyVar: {dict_bracketEqns_NotKeyVar} \nInBracketsTest: {InBracketTest}\n\n')



	#Substitute all equations by the key variable involving exponential, mulitplication, or division with a term subi where i denotes the number of substitutions__________________________________________________
	print(f'{">"*50} Subsitute terms with Exponentials/Multiplication/Division around the key child_var')
	InBracketTest = True
	testnum = 1
	print(f'\n{"*"*5}Check # {testnum}:')
	RHS_i, dict_bracketEqns,condition = SubExpMultDiv(RHS_i, child_var_i, list_mathOperations, dict_bracketEqns)
	print(f'for Check # {testnum}, RHS_i== {RHS_i}')
	testnum+=1	
	if len(dict_bracketEqns) != 0:
		child_var_i = max(dict_bracketEqns.keys())
		while condition == True:
			print(f'\n{"*"*5}Check # {testnum}:')
			RHS_i, dict_bracketEqns,condition = SubExpMultDiv(RHS_i, child_var_i, list_mathOperations, dict_bracketEqns)
			child_var_i = max(dict_bracketEqns.keys())
			print(f'for Check # {testnum}, RHS_i== {RHS_i}')
			# print(f'\nStep - Var inside bracket) \nRHS: {RHS} \ndict_bracketEqns: {dict_bracketEqns} \nInBracketsTest: {InBracketTest}')
			testnum+=1


	# #Begin reversing the math operations; beginning with adding/subtracting the NOT KEY TERMS
	# print(f'\n\n{">"*50} Begin RERVERSING LHS and RHS starting with ADDING/SUBTRACTING THE NOT KEY TERMS')
	# print(f'LHS:: {LHS}')
	# print(f'RHS:: {RHS_i}')
	# LHS_i = LHS
	# testnum = 1
	# print(f'\n{"*"*5}Check # {testnum}:')
	# LHS_i, RHS_i, condition = RevNK_AddSub(LHS, RHS_i, list_mathOperations, dict_bracketEqns, dict_bracketEqns_NotKeyVar, dict_reverse)
	# print(f'for Check # {testnum}, LHS_i=={LHS_i}   AND  RHS_i== {RHS_i}')
	# testnum+=1
	# while condition:
	# 	print(f'\n{"*"*5}Check # {testnum}:')
	# 	LHS_i, RHS_i, condition = RevNK_AddSub(LHS_i, RHS_i, list_mathOperations, dict_bracketEqns, dict_bracketEqns_NotKeyVar, dict_reverse)
	# 	print(f'for Check # {testnum}, LHS_i=={LHS_i}   AND  RHS_i== {RHS_i}')
	# 	if testnum>5:
	# 		break
	# 	testnum+=1
	# #now the first run through of reversing the addition and subtraction is complete, the RHS_i has been isolated to the max_var subi where i==i,max

	LHS_i = LHS
	LHS_i, RHS_i = Loop_RevNK_AddSub(LHS_i, RHS_i, list_mathOperations, dict_bracketEqns, dict_bracketEqns_NotKeyVar, dict_reverse)


	#replace in max_var
	ReplaceNum = 1
	#while len(dict_bracketEqns) !=0:
	max_var = max(dict_bracketEqns.keys())
	print('max_var == {max_var}')
	RHS_i = RHS_i.replace(max_var,dict_bracketEqns[max_var])
	del dict_bracketEqns[max_var]
	print(f'\n{"__"*15}Replacement #{ReplaceNum}{"__"*35}')
	print(f'with replacements in RHS_i is:: {RHS_i}')

	# RHS_i = '3-sub4+2' #this was a test to see that the following would be executed successfully
	if ('+' in RHS_i) | ('-' in RHS_i):
		LHS_i, RHS_i = Loop_RevNK_AddSub(LHS_i, RHS_i, list_mathOperations, dict_bracketEqns, dict_bracketEqns_NotKeyVar, dict_reverse)





def main():
	str1 = r'y=(w,n+2)-1*w,n'
	str1 = r'y=(w,n+2)-1'
	str1 = r'y=(2*(w,n+2))^2-1'
	str1 = r'y=(2*(w,n+2))^(2*3)-1'
	str1 = r'y=(2*(w,n+2))^(2*3)-((3*6)+2)+(3/2)'
	str1 = r'y=32*(2*(w,n+2))^(2*3)-((3*6)+2)'
	str1 = r'y=-((3*6)+2)-32*(2*(w,n+2))^(2*3)*5-25'
	dict_reverse={'+':'-','-':'+'}
	list_mathOperations = '+ - / * ^ ='.split()
	child_var = 'w,n'
	reverse_eqn = ReverseEqn(str1, dict_reverse, child_var, list_mathOperations)
	# print(reverse_eqn)
main()




