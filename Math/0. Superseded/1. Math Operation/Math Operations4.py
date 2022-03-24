#2020-10-26
#given a string with a math equation, program performs the operations in the proper operation

import re

def FindMultiInstances(str1, character):
	list_idx = []
	for idx, item in enumerate(str1):
		if item == character:
			list_idx.append(idx)
	print(f'There are {len(list_idx)} instances of character "{character}"')
	print(f'List of idxs for character: {list_idx}')
	return list_idx


class Math_NoBrackets():
    def __init__(self,str1):
        self.eqn = str1
        
        #get list of the math operations
        list_operators =[]
        list_mathOperators = '+ - * / ^'.split()
        for character in str1:
            if character in list_mathOperators:
                # print(character)
                list_operators.append(character)
        self.list_operators = list_operators
        print(f'List of Operators in string: {self.list_operators}')

        #get the list of the numbers in string
        list_eqn_splitUp = re.split('[+-/*^]',self.eqn)
        list_eqn_splitUp = [int(x) for x in list_eqn_splitUp]
        self.ListNumbers = list_eqn_splitUp
        print(f'List of all the numbers: {self.ListNumbers}')  

    def Exponential(self):
        print(f'\n{"*"*10} Execute all exponentials{"_"*50}')
        while True:
          try:
            step=1
            idx_div = self.list_operators.index('^')
            list_eqn_splitUp = self.ListNumbers
            list_operators = self.list_operators
            # print(idx_div)
  
            print(f'Step {step}) {list_eqn_splitUp}')
            step+=1

            num_i = list_eqn_splitUp[idx_div]**list_eqn_splitUp[idx_div+1]
            # print(f'{list_eqn_splitUp[idx_div+1]}')
            # print(f'num_i = {num_i}')
            list_eqn_splitUp[idx_div]=num_i
            del list_eqn_splitUp[idx_div+1]
            del list_operators[idx_div]
            print(f'Step {step}) {list_eqn_splitUp}')
            step+=1
            print(list_operators)
          except:
            print('end of Exponential')        
            break
    
    def Multiplification(self):
        print(f'\n{"*"*10} Execute all multiplification{"_"*50}')
        while True:
          try:
            step=1
            idx_div = self.list_operators.index('*')
            list_eqn_splitUp = self.ListNumbers
            list_operators = self.list_operators
            # print(idx_div)
  
            print(f'Step {step}) {list_eqn_splitUp}')
            step+=1

            num_i = list_eqn_splitUp[idx_div]*list_eqn_splitUp[idx_div+1]
            # print(f'{list_eqn_splitUp[idx_div+1]}')
            # print(f'num_i = {num_i}')
            list_eqn_splitUp[idx_div]=num_i
            del list_eqn_splitUp[idx_div+1]
            del list_operators[idx_div]
            print(f'Step {step}) {list_eqn_splitUp}')
            step+=1
            print(list_operators)
          except:
            print('end of Multiplification')        
            break

    def Division(self):
        print(f'\n{"*"*10} Execute all division{"_"*50}')
        while True:
          try:
            step=1
            idx_div = self.list_operators.index('/')
            list_eqn_splitUp = self.ListNumbers
            list_operators = self.list_operators
            # print(idx_div)
  
            print(f'Step {step}) {list_eqn_splitUp}')
            step+=1

            num_i = list_eqn_splitUp[idx_div]/list_eqn_splitUp[idx_div+1]
            # print(f'{list_eqn_splitUp[idx_div+1]}')
            # print(f'num_i = {num_i}')
            list_eqn_splitUp[idx_div]=num_i
            del list_eqn_splitUp[idx_div+1]
            del list_operators[idx_div]
            print(f'Step {step}) {list_eqn_splitUp}')
            step+=1
            print(list_operators)
          except:
            print('end of Division')        
            break

    def Addition(self):
        print(f'\n{"*"*10} Execute all Addition{"_"*50}')
        while True:
          try:
            step=1
            idx_div = self.list_operators.index('+')
            list_eqn_splitUp = self.ListNumbers
            list_operators = self.list_operators
            # print(idx_div)
  
            print(f'Step {step}) {list_eqn_splitUp}')
            step+=1

            num_i = list_eqn_splitUp[idx_div]+list_eqn_splitUp[idx_div+1]
            # print(f'{list_eqn_splitUp[idx_div+1]}')
            # print(f'num_i = {num_i}')
            list_eqn_splitUp[idx_div]=num_i
            del list_eqn_splitUp[idx_div+1]
            del list_operators[idx_div]
            print(f'Step {step}) {list_eqn_splitUp}')
            step+=1
            print(list_operators)
          except:
            print('end of Addition')        
            break

    def Subtraction(self):
        print(f'\n{"*"*10} Execute all Subtraction{"_"*50}')
        while True:
          try:
            step=1
            idx_div = self.list_operators.index('-')
            list_eqn_splitUp = self.ListNumbers
            list_operators = self.list_operators
            # print(idx_div)
  
            print(f'Step {step}) {list_eqn_splitUp}')
            step+=1

            num_i = list_eqn_splitUp[idx_div]-list_eqn_splitUp[idx_div+1]
            # print(f'{list_eqn_splitUp[idx_div+1]}')
            # print(f'num_i = {num_i}')
            list_eqn_splitUp[idx_div]=num_i
            del list_eqn_splitUp[idx_div+1]
            del list_operators[idx_div]
            print(f'Step {step}) {list_eqn_splitUp}')
            step+=1
            print(list_operators)
          except:
            print('end of Subtraction')        
            break

    def Run(self):
        Math_NoBrackets.Exponential(self)
        Math_NoBrackets.Multiplification(self)
        Math_NoBrackets.Division(self)
        Math_NoBrackets.Addition(self)
        Math_NoBrackets.Subtraction(self)
        return self.ListNumbers[0]


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
	    calc_noBrack = Math_NoBrackets(eqn_InBracket)
	    answer = calc_noBrack.Run()
	    print(f'\nFinal answer is "  {answer} "')


	    original_str = self.eqn
	    if idx0_low!=0:
	    	idx0_low-=1
	    if idx0_high != len(self.eqn)-1:
	    	idx0_high+=1

	    new_str = self.eqn[0:idx0_low]+f"{answer}"+self.eqn[idx0_high:]
	    self.eqn = new_str
	    print(f'\t {">"*75}>Updated equation string: "  {self.eqn}  "')

	    return self.eqn



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
	str_math = r"2+25*(312+(22/2))^2-38^3"
	calc = Math(str_math)
	break_loop = 0

	#complete all the math inside brackets
	while True:
		print('\n\n')
		# if break_loop>5:
		# 	break
		calc_i,idx0_low,idx0_high,completion = calc.BracketIdxs()
		print(calc_i, idx0_low, idx0_high)
		print(str_math[idx0_low-1:idx0_high+1])
		eqn_str = calc.MathOperations(calc_i, idx0_low,idx0_high)
		if completion == True:
			print('***No more brackets!\n\n')
			break
		break_loop+=1


	calc_noBrack = Math_NoBrackets(eqn_str)
	answer = calc_noBrack.Run()
	print(answer)


	# math_in_bracket = calc.InsideBracket()
	# num = calc.MathOperations(math_in_bracket)
	# print(num)

main()













