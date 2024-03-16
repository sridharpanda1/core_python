#WAP to check wheather the given number is between 1 and 100
n=int(input('Enter a number: '))
if n in range(1,101):
	print(f'{n} is in between 1 and 100')
else:
	print(f'{n} is out of range')