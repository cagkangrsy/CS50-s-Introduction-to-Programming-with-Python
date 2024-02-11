expression = input("Enter your operation as x + y ").split(" ")
no1 = int(expression[0])
operator = expression[1]
no2 = int(expression[2])
if operator == '+':
    result = float(no1 + no2)
elif operator == '-':
    result = float(no1 - no2)
elif operator == '*':
    result = float(no1 * no2)
else:
    result = float(no1 / no2)
print(result)
