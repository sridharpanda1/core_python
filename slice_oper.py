'''
Slice Operator:
	1. s[begin:end:step]
	for begin, end and step attributes, we can take either +ve or -ve values

	if step is +ve, than forward direction (left to right) and we have to consider from begin to end -1
	if step is -ve, than backward direction (right to left) and we have to cosider from begin to end +1
	if step is 0, than we will get error

	Note:
		in forward direction, if end is 0, than result will be empty string
		in backward direction, if end is -1, than result will be empty string

'''

#s = 'abcdefghijklmnopqrstuvwxyz'
s = 'ABCDEFGHIJ'
print(s[1:7])
print(s[:7])
print(s[1:])
print(s[:])
print(s[1:7:1])
print(s[1:15:1])
print(s[1:15:2])
print(s[1:15:3])
print(s[::1])
print(len(s))
print(s[::-1]) #reverse string
print(s[-1:-len(s)-1:-1])
print(s[1:6:2]) #BDF
print(s[::1]) #ABCDEFGHIJ
print(s[::-1])#JIHGFEDCBA
print(s[3:7:-1])# empty string
print(s[7:4:-1])#HGF
print(s[0:1000:-1])#empty string
print(s[0:1000:1])#ABCDEFGHIJ
print(s[-4:1:-1])#GFEDC
print(s[-4:1:-2])#GEC
print(s[5:0:1])
#print(s[5:0:0])#error
print(s[0:-10:-1])#empty