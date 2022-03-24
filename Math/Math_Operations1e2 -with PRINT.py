#2020-10-26
#given a string with a math equation, program performs the operations in the proper operation

import re, math, decimal

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
        print(list_idxStart, list_idxranges)
        print(list_idxranges)

        #this reviews the various bracket operations that must be executed
        for idx, entry in enumerate(list_idxranges):
            idx_low = int(entry.split(':')[0])+1
            idx_high = int(entry.split(':')[1])
            print(self.eqn[idx_low:idx_high])

            #the first entry is the first bracket that must be solved
            if idx ==0:
                str_mathfirst=self.eqn[idx_low:idx_high]
                idx0_low=idx_low
                idx0_high=idx_high              
                print(self.eqn[idx_low-3:idx_low])
                if self.eqn[idx_low-3:idx_low-1] == "ln":
                    func = 'ln'
                elif self.eqn[idx_low-4:idx_low-1] == 'log':
                    func = 'log'
                elif self.eqn[idx0_low-4:idx0_low-1] == 'exp':
                    func = 'exp'
                elif self.eqn[idx0_low-5:idx0_low-1] == 'atan':
                    func = 'atan'
                elif self.eqn[idx0_low-5:idx0_low-1] == 'asin':
                    func = 'asin'
                elif self.eqn[idx0_low-4:idx0_low-1] == 'acos':
                    func = 'acos'
                elif self.eqn[idx0_low-4:idx0_low-1] == 'sin':
                    func = 'sin'
                elif self.eqn[idx0_low-4:idx0_low-1] == 'tan':
                    func = 'tan'
                elif self.eqn[idx0_low-4:idx0_low-1] == 'cos':
                    func = 'cos'                    

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
        elif func == 'tan':
            num_i = math.tan(number)
        elif func == 'sin':
            num_i = math.sin(number)
        elif func == 'cos':
            num_i = math.cos(number)
        elif func == 'atan':
            num_i = math.atan(number)
        #there will be an error here if number >1
        elif func == 'asin':
            num_i = math.asin(number)
        elif func == 'acos':
            num_i = math.acos(number)
        print(num_i)
        print(self.eqn)
        print(self.eqn[idx0_low-1-len(func):idx0_high+1])
        self.eqn = self.eqn[:idx0_low-len(func)-1] + f'{num_i}' + self.eqn[idx0_high+1:]
        print(f'{self.eqn}\n{"_"*100}\n\n')

        return self.eqn


class Math_NoBrackets():
    def __init__(self,str1):
        self.eqn = str1.replace('pi',f'{math.pi}')
        str1 = str1.replace('pi', f'{math.pi}')
        print(f'String of Math_NoBrackets: {str1}')
        
        # #get list of the math operations
        # list_operators =[]
        list_mathOperators = '+ - * / ^'.split()
        # FirstCharNegative=False
        # for idx,character in enumerate(str1):
        #     if (idx==0) & (character=='-'):
        #         FirstCharNegative=True
        #         continue
        #     if character in list_mathOperators:
        #         if (character == '-') & (str1[idx-1] not in list_mathOperators):
        #             print(character)
        #             list_operators.append(character)
        # self.list_operators = list_operators
        # print(f'List of Operators in string: {self.list_operators}')

        # #get the list of the numbers in string
        # # list_eqn_splitUp = re.split('[+-/*^]',self.eqn)
        # # list_eqn_splitUp = [float(x.replace('(',"").replace(')',"")) for x in list_eqn_splitUp]
        # list_eqn_splitUp = re.findall(r'[+-]?\d*\.\d+|\d+',str1)
        # if FirstCharNegative==True:
        #     list_eqn_splitUp[0]=-1*float(list_eqn_splitUp[0])
        # list_eqn_splitUp = [float(x) for x in list_eqn_splitUp]
        # self.ListNumbers = list_eqn_splitUp
        # print(f'List of all the numbers: {self.ListNumbers}')  


        #find decimal nums
        floatNum =''
        list_numbers, list_strOperators = [],[]
        NegNum = False
        for idx, character in enumerate(str1):
            # print(character)
            if character in list_mathOperators:
                if len(floatNum)>0:
                    if floatNum[-1] == 'e':
                        floatNum+=character
                        continue
                print(f'floatNum == "{floatNum}"')
                
                if ((character == '-') & (idx>0) & (str1[idx-1] in list_mathOperators)) | ((idx==0) &(str1[idx]=='-')):
                    NegNum = True
                    continue

                if NegNum == True:
                    if 'e' in floatNum:
                        print(f'floatNum.split("e")[0] == {floatNum.split("e")[0]}')
                        print(f'floatNum.split("e")[1] == {float(floatNum.split("e")[1])}  {"*"*45}')
                        floatNum=float(floatNum.split('e')[0])*10**(float(floatNum.split('e')[1]))
                    list_numbers.append(-1*float(floatNum))
                    NegNum=False
                else:
                    if floatNum != '':
                        if 'e' in floatNum:
                            print(f'floatNum.split("e")[0] == {floatNum.split("e")[0]}')
                            print(f'floatNum.split("e")[1] == {float(floatNum.split("e")[1])}  {"*"*45}')
                            floatNum=float(floatNum.split('e')[0])*10**(float(floatNum.split('e')[1]))
                        list_numbers.append(float(floatNum))
                list_strOperators.append(character)

                floatNum=''
                continue
            # print(character)
            floatNum+=character
        if NegNum == True:
            list_numbers.append(-1*float(floatNum))
            NegNum=False
        else:
            print(f'single number == {floatNum}')
            list_numbers.append(float(floatNum))
            print('what the hell????')    
        print(list_numbers)
        print(list_strOperators)
        self.list_operators = list_strOperators
        self.ListNumbers = list_numbers






    def Exponential(self):
        print(f'\n{"*"*10} Execute all exponentials{"_"*50}')
        while True:
          try:
            step=1
            idx_div = self.list_operators.index('^')
            list_eqn_splitUp = self.ListNumbers
            list_operators = self.list_operators
            print(idx_div)
  
            print(f'Step {step}) {list_eqn_splitUp}')
            step+=1

            num_i = list_eqn_splitUp[idx_div]**list_eqn_splitUp[idx_div+1]
            print(f'{list_eqn_splitUp[idx_div+1]}')
            print(f'num_i = {num_i}')
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
            step=1
            try:

            
                idx_div = self.list_operators.index('*')
                list_eqn_splitUp = self.ListNumbers
                list_operators = self.list_operators
                print(f'idx_div=="{idx_div}"')
      
                print(f'Step {step}) {list_eqn_splitUp}')
                step+=1

                num_i = list_eqn_splitUp[idx_div]*list_eqn_splitUp[idx_div+1]
                print(f'{list_eqn_splitUp[idx_div+1]}')
                print(f'num_i={list_eqn_splitUp[idx_div]}*{list_eqn_splitUp[idx_div+1]}')
                print(f'num_i = {num_i}')
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
            print(idx_div)
  
            print(f'Step {step}) {list_eqn_splitUp}')
            step+=1

            num_i = list_eqn_splitUp[idx_div]/list_eqn_splitUp[idx_div+1]
            print(f'{list_eqn_splitUp[idx_div+1]}')
            print(f'num_i = {num_i}')
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
            print(idx_div)
  
            print(f'Step {step}) {list_eqn_splitUp}')
            step+=1

            num_i = list_eqn_splitUp[idx_div]+list_eqn_splitUp[idx_div+1]
            print(f'{list_eqn_splitUp[idx_div+1]}')
            print(f'num_i = {num_i}')
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
            print(idx_div)
  
            print(f'Step {step}) {list_eqn_splitUp}')
            step+=1

            num_i = list_eqn_splitUp[idx_div]-list_eqn_splitUp[idx_div+1]
            print(f'{list_eqn_splitUp[idx_div+1]}')
            print(f'num_i = {num_i}')
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
        self.eqn = math_str.replace('pi',f'{math.pi}')
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
        print(list_idxStart, list_idxranges)

        #this reviews the various bracket operations that must be executed
        for idx, entry in enumerate(list_idxranges):
            idx_low = int(entry.split(':')[0])+1
            idx_high = int(entry.split(':')[1])
            print(f'self.eqn[idx_low:idx_high] =="{self.eqn[idx_low:idx_high]}"')

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
        list_mathOperators = '+ - * / ^'.split()
        original_str = self.eqn
        if idx0_low!=0:
            idx0_low-=1
        # if idx0_high != len(self.eqn)-1:
        #     idx0_high+=1 #so idx0_high is the index for the ")" or "]", adding one here includes the bracket
        print(f'self.eqn == {self.eqn}')

        print(f'idx0_high == {idx0_high}')
        print(f'len(self.eqn) == {len(self.eqn)}')
        # if idx0_high < len(self.eqn)-2:
        #     if (self.eqn[idx0_high] in list_mathOperators):
        #         print('character found in list_mathOperators')
        #         idx0_high-=1
        print(f'{"^"*50}from idx0_low to idx0_high:: {self.eqn[idx0_low:idx0_high+1]}')
        if (idx0_low == 0) & (idx0_high == len(self.eqn)-1):
            new_str = f"{answer}"
        else:
            new_str = self.eqn[0:idx0_low]+f"{answer}"+self.eqn[idx0_high+1:]
        self.eqn = new_str
        print(f'\t {">"*75}>Updated equation string: "  {self.eqn}  "')

        return self.eqn

    def RunTillNoBrackets(self):
        #complete all the math inside all of the brackets
        while True:
            print('\n\n')
            # if break_loop>5:
            #   break
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

def CalcFromStr(str_math, decimal_accuracy):
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


    FinalAnswer = round(decimal.Decimal(FinalAnswer), decimal_accuracy)
    print(f'{"*"*50} Final Answer:   {FinalAnswer}')

    return FinalAnswer


def main():
    decimal_accuracy = 4

    str_math = r"2+25*(312+(22/2))^2-38^3"
    str_math = r"exp{(5-2)*3}*[3]" #5a
    str_math = r"exp{(5-2)*3}*ln{(5)}" #5b - confirm script can do multiple special expressions
    # str_math = r"2*exp{(5-2)*3}*[ln{(5)}-5*100]" #5b - confirm script can do multiple special calcs and brackets
    # str_math = r"3*2" #5b - confirm script can still capture no brackets
    str_math = r"ln{(7.7/3.3)}/(2*pi*8)"
    str_math = r"atan{(2*3-1)}*[ln{(3)}+2]"
    str_math = r"asin{(0.25)}*[ln{(3)}+2]"
    str_math = r"1/(2*pi*5.0)*ln{(22.0/3.0)}"
    str_math = r"2*pi/0.28"
    str_math=r'(500.0*1000/5308634.2999)*(1/(1-0.9980^2))'
    str_math = r'22.0000*cos{(22.4852*1.0)}+23.5230*sin{(22.4852*1.0)}'
    str_math = r'((50.0*1000/3500000.0)*1000*(3.1623/3.1280)*((2*(0.1468^2)*1.2418)-1.2418*(1-1.2418^2))/((1-1.2418^2)^2+(2*0.1468*1.2418)^2))+(10.0+(5.0*3.1623*0.1468))/3.1280'
    str_math = r'atan{((2*0.1468*1.2418)/(1-1.2418^2))}'
    str_math = r'(1/3500000.0)*(1/((1-1.2418^2)^2+(2*0.1468*1.2418)^2))*[(0.0000*(1-1.2418^2)^2-(2*63.6620*0.1468*1.2418))*cos{(1.0*3.9270*1.0)}+((2*0.0000*0.1468*1.2418)+63.6620*(1-1.2418^2))*sin{(1.0*3.9270*1.0)}]'
    str_math = r'(1.0/120971467.3099)*1000*1000*[1-(exp{(-1*0.0372*62.8754*1.0)})*[cos{(62.8319*1.0)}+0.0372*(62.8754/62.8319)*sin{(62.8319*1.0)}]]'
    # str_math = r'cos{(62.8319*1.0)}'
    # str_math = r'25e-2'
    # str_math = r'3.1623*[1-5.1387^2]^0.5' #yes, it does run into an error
    # str_math = r'22.0000*-0.8804189170827068+-23.5230*-0.47419672124859086'
    # str_math = r'[-1*10/2]^(-1*2)'
    # str_math = r'100^0.5'
    # str_math = r"asin{(1.1)}*[ln{(3)}+2]" #this will cause an error, asin(num>1) causes error


    FinalAnswer = CalcFromStr(str_math, decimal_accuracy)
    print(FinalAnswer)



main()













