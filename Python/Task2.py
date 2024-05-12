print("==Welcome to Simple Calculator application==")
choice=1
while(choice):
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    operator=input("Enter the operator(+,-,*,/,%,//,**):")
    if(operator=='+'):
        result=num1+num2
        print(f'The sum of {num1} and {num2} is {result}')
    if(operator=='-'):
        result=num1-num2
        print(f'The difference of {num1} and {num2} is {result}')
    if(operator=='*'):
        result=num1*num2
        print(f'The Multiplication of {num1} and {num2} is {result}')
    if(operator=='/'):
        if(num2!=0):
            result=num1/num2
            print(f'The division of {num1} by {num2} is {result}')
        else:
            print('Cannot divide by zero')
    
    if(operator=='**'):
        if(num1!=0 or num2!=0):
            result=num1**num2
            print(f'{num1} power {num2} is {result}')
        else:
            print("Don't write 0 for both num1 and num2")
    if(operator=='%'):
        if(num2!=0):
            result=num1%num2
            print(f'The Modulo of {num1} and {num2} is {result}')
        else:
            print('Modulo by zero is undefined')
    if(operator=='//'):
        if(num2!=0):
            result=num1//num2
            print(f'The floor division of {num1} and {num2} is {result}')
        else:
            print("floor division by zero is undefined")
    print("1. To continue more opertion:")
    print("0. Quit:")
    choice=int(input("Enter your choice: "))
print("Thanks for using Simple Calculator Application.")