lst = eval(input('Enter a list:'))
summ =  0
for l in lst:
	summ = l+summ
print(f'The sum of {lst} is {summ}')