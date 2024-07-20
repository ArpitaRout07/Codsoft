#simple Calculator

firstNum =int(input("Enter the first number: "))
secondNum = int(input("Enter the second number: "))
operator = input("Enter operator(+,-,*,/,%): ")

if operator =="+":
    print("The Addition is",firstNum+secondNum)
elif operator =="-":
    print("The Substraction is",firstNum-secondNum)
elif operator =="*":
    print("The Multiplication is",firstNum*secondNum)
elif operator =="/":
    print("The Division is",firstNum/secondNum)        
elif operator =="%":
    print("The Remainder is",firstNum%secondNum)
else: 
    print("invalid operator")