import random
import array 
password_length = 16
Digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Upper_Case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
Lower_Case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
Char_Symbol = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','/','`','~']
x = Lower_Case + Upper_Case+ Digit+ Char_Symbol

randoms_U = random.choice(Upper_Case)
randoms_L = random.choice(Lower_Case)
randoms_D = random.choice(Digit)
randoms_C = random.choice(Char_Symbol)

y = randoms_U + randoms_L + randoms_D + randoms_C

password = ""
for i in range(password_length - 4):
	y = y + random.choice(x)

	z = array.array('u',y)
	random.shuffle(z)

for p in z:
	password= password+p
print(f'print Your password : {password}')
'''
print('press 1 to generate another password :)')
print('or')
print('press 2 to not generate another password :)')

new_password = ""
for i in range(password_length - 4):
	ya = y + random.choice(x)

	u = array.array('u',ya)
	random.shuffle(u)

for r in u:
	new_password= new_password+r

new_pass = int(input())
if (new_pass==1):
	print(f'Your New Password is : {new_password}')
else:
	print('Thanks')

'''

