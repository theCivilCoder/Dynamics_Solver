import math, re, openpyxl, pandas as pd, numpy as np, shutil,os, datetime
from decimal import *

import sys
sys.path.insert(1, r'C:\Users\yongj\Documents\Coding\Python\1. Projects\Math')
from Math_Operations import CalcFromStr

def GetExcelInputs(path_input, cell_types, cell_qnType):
	#get the type of questions this Input workbook has the inputs and outputs for
	wb = openpyxl.load_workbook(filename=path_input, read_only=False, keep_vba=True)
	ws = wb['Start']

	#get qn type for specific problem
	qnType = ws[cell_qnType].value
	ws = wb[qnType]

	#get all the qn types from excel
	col_IDnum = cell_types[0]
	col_Types = chr(ord(cell_types[0])+1)
	col_RelSections = chr(ord(cell_types[0])+2)
	row = int(cell_types[1:])
	dict_types = {}
	while True:
		# if row>10:
		# 	break
		IDnum = ws[col_IDnum+str(row)].value
		Type = ws[col_Types+str(row)].value
		RelSections = ws[col_RelSections+str(row)].value

		if IDnum == None:
			break

		RelSections = str(RelSections).replace(' ','').split(',')
		RelSections = [int(x) for x in RelSections]
		# print(RelSections)
		
		# dict_types[Type]=IDnum
		dict_types[Type]=RelSections
		row+=1
	print(dict_types)
	
	qn_type = ws[cell_qnType].value
	print(f'{"*"*25}  QUESTION TYPE:::   {qn_type}')

	#Get the inputs
	df = pd.read_excel(path_input, sheet_name= qn_type, nrows=200 ,usecols="A:D", skiprows=2)
	# print(df)

	filt = df.Section.isin(dict_types[qn_type])
	# print(df[filt])
	df_filt = df[filt]

	return df_filt, qnType



def ReplaceSingleVar(str1, var_i, Replacement):
	new_str =''
	for idx, character in enumerate(str1):
		if idx < len(str1)-1:
			if (character == var_i) & ((str1[idx+1].isalpha()) or (str1[idx+1]==',')):
				new_str+=character
			elif character == var_i:
				new_str+=Replacement
			else:
				new_str+=character
		else:
			if (character == var_i):
				new_str+=Replacement
			else:
				new_str+=character
	return new_str


#function will sub in inputs within df_input into dict_vars	
def SubInputs(df_input, dict_vars, decimal_accuracy, var_testSINGLE):
	# get the values of inputs available
	df_inputOnly = df_input.copy().dropna(axis=0,subset=['Input']).set_index('Parameter')
	# print(df_inputOnly)
	# print(df_input)

	df_new = df_input.copy().dropna(axis=0,subset=['Parameter']).set_index('Parameter')
	df_new = df_new.replace({np.nan: None})
	# print(df_new)

	print(f'\n{"_"*25} Solving for Unknowns')
	# print(f'dict_vars:: \n{dict_vars}')
	var_testCONDITION = False
	#run this loop 10 times to resolve equations

	test = 0
	while test < 10:
		# print(df_input)
		df_inputOnly = df_new.copy().dropna(axis=0,subset=['Input'])
		# print(f'{"__"*10}df_InputsOnly is:: \n{df_inputOnly}')

		# df_new = df_new.dropna(axis=0, subset=['Parameter'])
		# print(f'\n{">"*5}Updated df_new for this iterations::\n{df_new}')

		#substitue in inputs and solve where possible
		for var_i in df_new.index:
			# print(var_i, type(var_i))
			value = df_new.loc[var_i, 'Input']
			# print(var_i,value)
			# print(f'this is np.nan: {np.nan}')
			if value == None:
				# print(var_i, value)
				# eqn = dict_vars[var_i]
				# print(eqn)

				#replace the knowns into the eqn string
				for known_var in df_inputOnly.index:
					# print(f'known_var is {known_var}')
					if len(known_var) == 1:
						#this function will only replace the single variable because ".replace" would replace 'c' with a value in the 'cos()'
						dict_vars[var_i] = ReplaceSingleVar(dict_vars[var_i], known_var, f'{df_inputOnly.loc[known_var,"Input"]}')    #Function:: ReplaceSingleVar(str1, var_i, Replacement) 
					else:
						dict_vars[var_i] = dict_vars[var_i].replace(known_var, f'{df_inputOnly.loc[known_var,"Input"]}')


				#check if there are any special math functions inside equation, remove for testsing
				list_eqns_i = dict_vars[var_i].split('==')
				# print(list_eqns_i)

				#review specific variable where an error has been encountered
				# if var_i == 'w,D':
				# 	print(list_eqns_i)

				#execute logic  to calculate for a variable
				
				for eqn in list_eqns_i:
					list_specMath = 'pi exp ln log atan asin acos tan sin cos'.split()
					eqn_test = eqn
					for spec in list_specMath:
						if spec in eqn_test:
							eqn_test = eqn_test.replace(spec, '')
							# break
					# var_testSINGLE =  'u,t'#********************************************************************Check for error with a single variable
					if var_i==var_testSINGLE:
							var_testCONDITION=True
							var_testSINGLE_eqn = eqn_test
							var_testSINGLE_Calc = 'ERROR'

					list_letters = re.findall('[a-zA-Z]+', eqn_test) #check if any letters inside eqn
					if len(list_letters) == 0:
						print(var_i)
						print(f'eqn can be solved. Run the Math Operations Code on eqn: {eqn}')
						df_new.loc[var_i, 'Input']= f'{CalcFromStr(eqn, decimal_accuracy)}'
						if var_i==var_testSINGLE:
							print(f'{"%"*50}   eqn_test is {eqn_test}     {"<"*25}')
							var_testCONDITION=True
							var_testSINGLE_eqn = eqn_test
							var_testSINGLE_Calc = CalcFromStr(eqn, decimal_accuracy)
							print(f'{var_i} == {CalcFromStr(eqn, decimal_accuracy)}')

						# break				
					else:
						# print(list_letters)
						# print(f'eqn has letters inside:  {eqn}')
						pass
		test+=1
		df_answers = df_new
	print(f'\n\nFinal df_input:: \n{df_answers}')

	if var_testCONDITION==True:
		print(f'\n\nVariable under consideration:  {var_testSINGLE}\n \tEquation:: {var_testSINGLE_eqn}  \n\tResult::  {var_testSINGLE_Calc}')

	return df_answers

#copy excel then input answers
def NewExcel(path_input, cell_answers, df_answers,decimal_accuracy, qnType):
	FileNameExtension = datetime.datetime.today().strftime(f'SOLNS %Y-%m-%d %I-%M-%S %p {qnType}.xlsx')
	path2 =  path_input.replace('.xlsx',f'{FileNameExtension}')
	shutil.copyfile(path_input,path2)

	#get the type of questions this Input workbook has the inputs and outputs for
	wb = openpyxl.load_workbook(filename=path2, read_only=False)
	# ws = wb.worksheets[0]
	ws = wb[qnType]
	col_Param = cell_answers[0]
	col_Input = chr(ord(cell_answers[0])+1)
	col_SolnMarker = chr(ord(cell_answers[0])+4)
	row = int(cell_answers[1:])

	print(f'\n\nthis is df_answers:::\n {df_answers}')

	# print('so far so good')
	# print(df_answers)
	while True:
		var_i = ws[col_Param+str(row)].value
		input_i = ws[col_Input+str(row)].value
		if (row >125)|(var_i==None):
			break
		if input_i == None:
			# print(var_i)
			answer = df_answers.loc[var_i,'Input']
			if answer != None:
				ws[col_Input+str(row)]=round(Decimal(float(answer)),decimal_accuracy)
				ws[col_SolnMarker+str(row)]='Solved'
		# print(f'so far so good on row {row}')
		
		row+=1
	wb.save(path2)
	os.startfile(path2)




def ReadText_AllQntypes(path_text, FromExcelQnType):
	dict_QnTypes_FromTxt = {}
	f = open(path_text,'r')
	str_QnType =''
	linenum=1
	list_QnTypes, list_strEqns = [], []
	for line in f:
		if "****" in line:
			QnType = line.replace('****','').replace("\n",'').replace('_','')
			list_QnTypes.append(QnType)
			if linenum != 1:
				list_strEqns.append(str_QnType)
			str_QnType = ''
			# continue
		else:
			str_QnType+=line
			# print(line)
		linenum+=1
	list_strEqns.append(str_QnType)

	for idx,QnType in enumerate(list_QnTypes):
		str_QnType = list_strEqns[idx]
		dict_QnTypes_FromTxt[QnType]=str_QnType

	# print(f'\n\ndict_QnTypes_FromTxt=={dict_QnTypes_FromTxt}')
	print(f'\n\nfrom worksheet, qnType == "{FromExcelQnType}"')
	all_eqns_strsA = dict_QnTypes_FromTxt[FromExcelQnType]
	all_eqnsA = all_eqns_strsA.replace('\t','').split('\n')
	all_eqnsA = [x for x in all_eqnsA if len(x)>0]

	dict_eqns1 = {}
	for eqn in all_eqnsA:
		var = eqn.split('=',1)[0]
		eqn_vars = eqn.split('=',1)[1]
		dict_eqns1[var]=eqn_vars
	# print(dict_eqns1)

	# return dict_QnTypes_FromTxt
	return dict_eqns1






def main():
	var_testSINGLE = 'u,t'  #if the variable is calculated then it will be presented at the bottom of the results
	# NOTE that the equation presented will not include the special math equations: tan, sin, cos, ln, exp, etc
	print_to_excel = False
	print_to_excel = True

	# path_input = r'C:\Users\yongj\Downloads\2. Courses\10. ENCI639 Dynamics\0a. Python\1. Calc\ENCI639 Inputs.xlsx'
	path_input = r'C:\Users\yongj\Downloads\2. Courses\10. ENCI639 Dynamics\0. Other Docs\0a. Python\1. Calc\ENCI639 Inputs.xlsx'
	cell_types = 'H4'
	cell_qnType = 'B1'
	cell_answers = 'A4'
	decimal_accuracy=4

	df_input, qnType = GetExcelInputs(path_input, cell_types, cell_qnType)
	print(f'qnType == "{qnType}"')
	# print(df_input)

	path_Formulas = r'C:\Users\yongj\Downloads\2. Courses\10. ENCI639 Dynamics\0. Other Docs\0a. Python\1. Calc\Formulas.txt'
	dict_vars = ReadText_AllQntypes(path_Formulas, qnType)
	print(dict_vars)

	df_answers = SubInputs(df_input, dict_vars, decimal_accuracy, var_testSINGLE)

	#line 138 holds where I can set the variable that I want to review
	if print_to_excel:
		NewExcel(path_input, cell_answers, df_answers, decimal_accuracy, qnType)


main()