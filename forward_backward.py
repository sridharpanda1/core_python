#WAP to take a string and print all the charater in forward and backward direction.
s=input('ENter any string: ')
'''print('All forward Direction:')
i=0
N= len(s)
while i<N:
	print(s[i])
	i=i+1

print('All Backward Direction: ')
j=-1
while j>=-N:
	print(s[j])
	j=j-1'''
frd = s[::1]
bkd = s[::-1]
print('All forward Direction')
for x in frd:
	print(x)
print('All backward Direction')
for y in bkd:
	print(y)
