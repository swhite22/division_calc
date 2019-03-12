num1 = 0
num2 = 0
quotient = 0
remainder = 0
product = 0

num1 = int(input('Input your first number: '))
num2 = int(input('Input your second number: '))

quotient = num1//num2

print('your quotient is: ', quotient)

num1 = int(input('Please input another, new, number: '))
num2 = int(input('Please input another, new, number: '))

quotient = num1//num2
remainder = num1%num2
product = num1*num2


print('Your quotient is: ', quotient, ', with a remainder of: ', remainder, '. Your prodcut is product: ', product)
