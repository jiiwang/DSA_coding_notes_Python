def calculator(expr:str)->int:
    n = len(expr)
    stack = []

    i = 0
    while i < n:
        # print(f"idx: {i}, char at idx: {expr[i]}")
        if expr[i].isdecimal():
            # push num into stack
            num = 0
            while expr[i].isdecimal() and i < n:
                 num = num*10 + int(expr[i])
                 i+=1
            stack.append(num)
            i-=1

        if expr[i] == ")" and len(stack) >= 2:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1+num2) 
        
        i+=1
        # print(stack)
    
    return stack[-1]

# test cases
expr1 = "add(4,add(5,6))"
print(expr1)
print(f"output: {calculator(expr1)}") # Expected output: 15

expr2 = "add(add(2,1),add(5,6))"
print(expr2)
print(f"output: {calculator(expr2)}") # Expected output: 14

expr3 = "add(12,add(24,6))"
print(expr3)
print(f"output: {calculator(expr3)}") # Expected output: 42