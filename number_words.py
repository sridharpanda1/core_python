n = int(input('Enter a Number: '))
d = {0:'ZERO', 1:'ONE', 2:'TWO', 3:'THREE', 4:'FOUR', 5:'FIVE', 6:'SIX', 7:'SEVEN', 8:'EIGHT', 9:'NINE'}
DD = {2:'TWENTY', 3:'THIRTY', 4:'FOURTY', 5:'FIFTY', 6:'SIXTY', 7:'SEVENTY', 8:'EIGHTY', 9:'NINETY'}
DDD = {100:'ONE HUNDRED'}
spl = {10:'TEN', 11:'ELEVEN', 12:'TWELVE', 3:'THIRTEEN', 14:'FOURTEEN', 15:'FIFTEEN', 16:'SIXTEEN', 17:'SEVENTEEN', 18:'EIGHTEEN', 19:'NINETEEN'}
ten_digit = n//10
unit_digit = n%10

if n<10:
	op = d[n]
elif n>=10 and n<=19:
	op = spl[n]
elif n>19 and n<=99:
	if unit_digit == 0:
		op = DD[ten_digit]
	else:
		op = DD[ten_digit]+' '+d[unit_digit]
else:
	if n in range(101,110):
		op = DDD[100]+" "+d[unit_digit]
	elif n == 100:
		op = DDD[100]
	elif n in range(110,120):
		op = DDD[100]+" "+spl[n-100]
	elif n in range(120, 200) and n%10 == 0: 
		op = DDD[100]+" "+DD[ten_digit-10]
	else:
		op = DDD[100]+" "+DD[ten_digit-10]+' '+d[unit_digit]

print(f'{n} = {op}')