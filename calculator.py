def calculator(n1,n2,operator):
    if operator == "+":
        return n1+n2
    elif operator == "-":
        return n1-n2
    elif operator == "*":
        return n1*n2
    elif operator == "/":
        return n1/n2
    elif operator == "%":
        return n1%n2
    else:
        return f"{operator} is invalid."

print(calculator(20,10,"/"))