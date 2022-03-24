import re

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

def main():
    str1 = '25*12^2/2+38^1-2^3*2'
    calc = Math_NoBrackets(str1)
    answer = calc.Run()
    print(f'\nFinal answer is "  {answer} "')

main()

