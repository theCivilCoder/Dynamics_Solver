#2020-10-30
#all eqns for various question types is to be stored on Formulas
#this script will identify relationships for variables which have not been defined yet

import re, os

def EqnAssistant(path):

	#read through test file and save everything to single string
	f = open(path,'r')
	alleqns = ''
	for line in f:
		if '****' in line:
			QnType = line.replace('****','').replace('\n','')
			continue
		alleqns+=line
	# print(alleqns)
	f.close()

	#Process string into a dictionary where the key:value pairs has the variable as the key and the eqns as the value
	alleqns = alleqns.replace('\t','').split('\n')
	alleqns = [x for x in alleqns if len(x)>0]
	dict_eqns1={}
	for eqn in alleqns:
		var = eqn.split('=',1)[0]
		eqn_vars = eqn.split('=',1)[1]
		dict_eqns1[var]=eqn_vars
	print(dict_eqns1)

	#run through to check that the child variable has an eqn where it is related to the parent variable
	# var_i = 'u(t)'
	list_missing = []
	errorNum = 1
	for var_i in dict_eqns1.keys():
		test_eqns = dict_eqns1[var_i]
		# print(f'\ntest_eqns for {var_i} is:: {test_eqns}')
		list_specMath = 'pi exp ln log atan asin acos tan sin cos'.split()
		list_MoreRemoving = '-1 { } [ ] ( )'
		for spec in list_specMath:
			if spec in test_eqns:
				test_eqns = test_eqns.replace(spec,'')
		for extra in list_MoreRemoving:
			if extra in test_eqns:
				test_eqns = test_eqns.replace(extra,'')

		list_mathOperations = '+ - / * ^ ='.split()
		var_found = ''
		list_variables=[]
		for character in test_eqns:
			# print(character)
			if character in list_mathOperations:
				if var_found in list_variables:
					var_found=''
					continue
				list_variables.append(var_found)
				var_found=''
				continue
			var_found+=character
		list_variables=[x for x in list_variables if len(x)!=0]
		# list_NoNums = list_variables.copy()
		list_NoNums =[]
		for varNoNum in list_variables:
			try:
				float(varNoNum)
			except:
				list_NoNums.append(varNoNum)
		list_variables = list_NoNums.copy()
		print(f'\nfor var_i {var_i}, \nlist_variables == {list_variables}')

		
		for child_var in list_variables:
			try:
				child_eqn = dict_eqns1[child_var]
				# print(f'for child_var "{child_var}",  child_eqn == {child_eqn}')
				if var_i not in child_eqn:
					print(f'child_var "{child_var}" is missing a relation with the parent var "{var_i}"')
					list_missing.append(f'{errorNum})  child_var "{child_var}" is missing a relation with the parent var "{var_i}"')	
					errorNum+=1				
			except:
				list_missing.append(f'{errorNum})  Missing equation for the variable "{child_var}"')
				errorNum+=1
	print(f'\n\n{">"*10} This is the list of missing relations:\n{list_missing}')

	print(f'\nQnType = {QnType}')
	print(path)
	path2 = '\\'.join(path.split('\\')[:-1])+f'\\Missing Variable Eqns - {QnType}.txt'
	print(path2)

	g = open(path2,'w')
	for line in list_missing:
		g.write(line+'\n')
	g.close()

	os.startfile(path2)



def main():
	path = r"C:\Users\yongj\Documents\Coding\Python\1. Projects\Math\1. Equation Assistant\Formula_i.txt"
	EqnAssistant(path)

main()





