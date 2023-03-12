number1 = int(input("Digite o primeiro numero "))
number2 = int(input("Digite o segundo numero "))
number3 = int(input("Digite o terceiro numero "))

if number1 > number2 and number1 > number3:
    larger_number = number1
elif number2 > number1 and number2> number3:
    larger_number = number2
else:
    larger_number = number3

print(larger_number)