num1 = int(input('num1: '))
num2 = int(input('num2: '))
num3 = int(input('num3: '))
if num1 > num2 and num1 > num3:
    print(f'{num1} max')
elif num2 > num1 and num2 > num3:
    print(f'{num2} max')
elif num3 > num1 and num3 > num2:
    print(f'{num3} max')
