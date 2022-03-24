def findNegNums(str1):
	list_mathOperators = '+ - * / ^'.split()

	#find decimal nums
	floatNum =''
	list_numbers, list_strOperators = [],[]
	NegNum = False
	for idx, character in enumerate(str1):
		# print(character)
		if character in list_mathOperators:
			# print(f'floatNum == "{floatNum}"')
			
			if ((character == '-') & (idx>0) & (str1[idx-1] in list_mathOperators)) | ((idx==0) &(str1[idx]=='-')):
				NegNum = True
				continue

			if NegNum == True:
				list_numbers.append(-1*float(floatNum))
				NegNum=False
			else:
				if floatNum != '':
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
		list_numbers.append(float(floatNum))	
	print(list_numbers)
	print(list_strOperators)
	


def main():
	str1 = r'22.0000*-0.88+23.523*-0.4741'
	# str1 = r'-22.0000*-0.88+23.523*-0.4741'
	findNegNums(str1)

main()