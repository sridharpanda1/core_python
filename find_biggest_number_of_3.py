#WAP to find biggest of 2 given int values

n1 = int(input('Enter 1st Number: '))
n2 = int(input('Enter 2nd Number: '))
n3 = int(input('Enter 3rd Number: '))

if n1>n2 and n1>n3:
	print(f'{n1} is greater than {n2} and {n3}')
elif n2>n1 and n2>n3:
	print(f'{n2} is greater than {n1} and {n3}')
else:
	print(f'{n3} is greater than {n1} and {n2}')

