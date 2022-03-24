#2020-11-03

def ReadText_AllQntypes(path_text):
	dict_QnTypes_FromTxt = {}
	f = open(path_text,'r')
	str_QnType =''
	linenum=1
	list_QnTypes, list_strEqns = [], []
	for line in f:
		if "****" in line:
			QnType = line.replace('****','').replace("\n",'')
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

	# print(f'length of list_QnTypes:\n{len(list_QnTypes)}')
	# print(f'{list_QnTypes}')
	# print(f'\nlength of list_strEqns:\n{len(list_strEqns)}')

	for idx,QnType in enumerate(list_QnTypes):
		str_QnType = list_strEqns[idx]
		dict_QnTypes_FromTxt[QnType]=str_QnType

	return dict_QnTypes_FromTxt

def main():
	path_text = r'C:\Users\yongj\Downloads\2. Courses\10. ENCI639 Dynamics\0. Other Docs\0a. Python\1. Calc\Formulas.txt'
	dict_QnTypes_FromTxt = ReadText_AllQntypes(path_text)

	for key_i in list(dict_QnTypes_FromTxt.keys()):
		key_i = key_i.replace("\n","")
		print(f'{">"*25}for key={key_i}:')
		print(f'{dict_QnTypes_FromTxt[key_i]}')
	# print(dict_QnTypes_FromTxt)



main()




