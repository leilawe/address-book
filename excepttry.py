try: 
    num1=int(input("enter your first number: "))
    num2=int(input("enter your second number: "))

    print(int(num1 / num2))

except ZeroDivisionError:
    print("you can't divide by zero. ")

except ValueError:
    print("invalid input. please enter a number! ")  

