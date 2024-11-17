from collections import defaultdict


def simple_expr(expr:str)->str:
    # step 1: expand the expression
    expand_expr = []
    prev_sign = "+"
    parathesis = 0
    for char in expr:
        if char.isalpha():
            expand_expr.append(char)
        
        if char == "(":
            parathesis +=1
        
        if char == ")":
            parathesis -=1
        
        if char in "+-" and parathesis == 0:
            expand_expr.append(char)
            prev_sign = char

        if char in "+-" and parathesis == 1:
            if prev_sign == "+":
                expand_expr.append(char)
            else:
                expand_expr.append("+" if char == "-" else "-")

    print(expand_expr)

    # step2: get the coefficient
    coefficient = defaultdict(int)

    prev_sign = "+"
    for char in expand_expr:
        if char in "+-":
            prev_sign = char
        if char.isalpha():
            if prev_sign == "+":
                coefficient[char] += 1  
            else:
                coefficient[char] -= 1

    print(coefficient)

    # step 3: format output
    output_expr = []

    for key, value in coefficient.items():
        if value > 0:
            if value == 1:
                output_expr.extend(["+", key])
            else:
                output_expr.extend(["+", str(value), key])
        if value < 0:
            if value == -1:
                output_expr.extend(["-", key])
            else:
                output_expr.extend([str(value), key])

    output = "".join(output_expr)
    return output[1:] if output[0] == "+" else output

# test case
# exp = "a-(b-c)"
exp = "-a-a-(b-a)-b-(b+c)"

print(f"input expression: {exp}")
print(f"simplified expression: {simple_expr(exp)}")    # expected: "-a-3b-c"