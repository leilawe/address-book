def caculator(a,b,operator):
    if operator=="+":
        return a+b
    elif operator=="-":
        return a-b
    elif operator=="*":
        return a*b
    elif operator=="/":
        return a/b
    else:
        print("error")
        return 0

a=int(input("enter ur first number: "))
b=int(input("enter ur second number: "))
operator=input("enter ur opertor: ")
result= caculator(a,b,operator)
print(result)