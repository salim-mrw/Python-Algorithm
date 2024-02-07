def calculator(total):
	try:
		status = 'y'
		while status != 'n':
			process = str(input('process input + - * ÷ : '))
			if process == '+':
				number = int(input('number : '))
				total = total + number
			if process == '-':
				number = int(input('number : '))
				total = total - number
			if process == '*':
				number = int(input('number : '))
				total = total * number
			if process == '÷':
				number = int(input('number : '))
				total = total / number
			print('total is : ' + str(total))
			status = str(input('status input y or n :  '))
			if status == 'y':
				calculator(total)
	except:
		print('input deny')
		
if __name__ == '__main__':
	total = 0
	calculator(total)