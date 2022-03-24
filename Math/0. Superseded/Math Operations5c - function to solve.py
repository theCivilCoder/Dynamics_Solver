#2020-10-26
#given a string with a math equation, program performs the operations in the proper operation

import re, math

def FindMultiInstances(str1, character):
	list_idx = []
	for idx, item in enumerate(str1):
		if item == character:
			list_idx.append(idx)
	print(f'There are {len(list_idx)} instances of character "{character}"')
	print(f'List of idxs for character: {list_idx}')
	return list_idx

class SpecMath():
    def __init__(self,str1):
        self.eqn = str1
        self.completion = False

    def Check(self):
        if '{' in self.eqn:
            Check = True
        else:
            Check = False
        return Check

    def SpecialIdxs(self):
        list_idxStart, list_idxranges = [],[]
        list_specMath = 'ln log exp'.split()
        for idx,item in enumerate(self.eqn):
            if (item == '{'):
                list_idxStart.append(idx)       
            if (item == '}'):
                list_idxranges.append(f'{list_idxStart[-1]}:{idx}')
                list_idxStart.pop()
        # print(list_idxStart, list_idxranges)
        print(list_idxranges)

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
                # print(self.eqn[idx_low-3:idx_low])
                if self.eqn[idx_low-3:idx_low-1] == "ln":
                    func = 'ln'
                elif self.eqn[idx_low-4:idx_low-1] == 'log':
                    func = 'log'
                elif self.eqn[idx0_low-4:idx0_low-1] == 'exp':
                    func = 'exp'
                # else:
                #     func = 'NOT SPECIAL'
                print(f'string eqn: {str_mathfirst} :', idx0_low, idx0_high, func)

        if len(list_idxranges)==1:
            self.completion = True

        return str_mathfirst, idx0_low, idx0_high, self.completion,func

    def SpecOperation(self, func, number, idx0_low, idx0_high):
        if func == 'ln':
            num_i = math.log(number)
        elif func == 'log':
            num_i = math.log10(number)
        elif func == 'exp':
            num_i = math.exp(number)
        print(num_i)
        print(self.eqn)
        # print(self.eqn[idx0_low-1-len(func):idx0_high+1])
        self.eqn = self.eqn[:idx0_low-len(func)-1] + f'{num_i}' + self.eqn[idx0_high+1:]
        print(f'{self.eqn}\n{"_"*100}\n\n')

        return self.eqn


class Math_NoBrackets():
    def __init__(self,str1):
        self.eqn = str1
        print(f'String of Math_NoBrackets: {str1}')
        
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
        # list_eqn_splitUp = re.split('[+-/*^]',self.eqn)
        # list_eqn_splitUp = [float(x.replace('(',"").replace(')',"")) for x in list_eqn_splitUp]
        list_eqn_splitUp = re.findall(r'[+-]?\d*\.\d+|\d+',str1)
        list_eqn_splitUp = [float(x) for x in list_eqn_splitUp]
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
		print(f'self.eqn for BracketIdxs:  {self.eqn}')
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
				print(f'>>>idx0')
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

	def RunTillNoBrackets(self):
		#complete all the math inside all of the brackets
		while True:
			print('\n\n')
			# if break_loop>5:
			# 	break
			calc_i,idx0_low,idx0_high,completion =Math.BracketIdxs(self)
			print(calc_i, idx0_low, idx0_high)
			print(self.eqn[idx0_low-1:idx0_high+1])
			eqn_str = Math.MathOperations(self,calc_i, idx0_low,idx0_high)
			if completion == True:
				print('***No more brackets!\n\n')
				break
			# break_loop+=1
		calc_noBrack = Math_NoBrackets(eqn_str)
		answer = calc_noBrack.Run()
		print(answer)
		return answer

def CalcFromStr(str_math):
	# str_math = r"2+25*(312+(22/2))^2-38^3"
	# str_math = r"exp{(5-2)*3}*[3]" #5a
	# str_math = r"exp{(5-2)*3}*ln{(5)}" #5b - confirm script can do multiple special expressions
	# str_math = r"2*exp{(5-2)*3}*[ln{(5)}-5*100]" #5b - confirm script can do multiple special calcs and brackets
	# str_math = r"3*2" #5b - confirm script can still capture no brackets

	calc0 = SpecMath(str_math)
	check0 = calc0.Check()
	if check0 == True:
		completion = False

		while completion == False:
			str_mathfirst, idx0_low, idx0_high, completion,func = calc0.SpecialIdxs()
			##run existing code to resolve the string 'str_mathfirst'
			calc = Math(str_mathfirst)
			#Identifies all the brackets then runs all the math until answer is determined
			number = calc.RunTillNoBrackets()
			math_str = calc0.SpecOperation(func, number, idx0_low, idx0_high)
			print(f'{"<"*50} End of Iteration:  {math_str}  {">"*50}')
	else:
		print('No special functions in string (exp ln log)')
		math_str = str_math
		pass

	# Final = Math_NoBrackets(math_str)
	# FinalAnswer = Final.Run()
	print(f'math_str input at the end is {math_str}')
	
	if ('(' in math_str) or ('[' in math_str):
		Final = Math(math_str)
		FinalAnswer = Final.RunTillNoBrackets()
	else:
		Final = Math_NoBrackets(math_str)
		FinalAnswer = Final.Run()
	print(f'{"*"*50} Final Answer:   {FinalAnswer}')


def main():
	str_math = r"2+25*(312+(22/2))^2-38^3"
	str_math = r"exp{(5-2)*3}*[3]" #5a
	str_math = r"exp{(5-2)*3}*ln{(5)}" #5b - confirm script can do multiple special expressions
	# str_math = r"2*exp{(5-2)*3}*[ln{(5)}-5*100]" #5b - confirm script can do multiple special calcs and brackets
	# str_math = r"3*2" #5b - confirm script can still capture no brackets

	CalcFromStr(str_math)




main()













