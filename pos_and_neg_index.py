#WAP to read a string from keybord and display its charater by showing both +ve and -ve index
s= input('Enter a string: ')
i =  0
for s1 in s:
	print(f'The charater {s1} present at +ve index is: {i} and -ve index is {i-len(s)}')
	i = i+1