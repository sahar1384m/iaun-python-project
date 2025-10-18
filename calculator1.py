number1 = int(input("Enter your first Namber:"))
number2 = int(input("Enter your second Namber:"))
opration = input("Enter your opration:")
if (opration == '+'):
    print("result:" ,(number1 + number2))
elif (opration == '-'):
    print("result:" ,(number1 - number2))
elif (opration == '*'):
    print("result:" ,(number1 * number2))
elif (opration == '/'):
    print("result:" ,(number1 / number2))
elif (opration == '^'):
    print("result:" ,(number1 ** number2))
else:
    print("your opration is false!!!")