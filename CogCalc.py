


"""Cognitive Calculator...TBD: describe the features
    - operator: add, sub, mul, div
    - operand: list of numbers"""
def main(args):
    op = args["operator"]
    operands= args["operands"]
    if not operands:
        op = ""
    
    else:

        numbers = []
        for operand in operands:
            numbers.append(float(operand))

    
   
    result = 0
    status = "ok"



    
    if op == "add":
        value = add(numbers)
        result = value[0]
        status = value[1] 
    elif op == "sub":
        value = sub(numbers)
        result = value[0]
        status = value[1] 
    elif op == "mul":
        value = mul(numbers)
        result = value[0]
        status = value[1] 
    elif op == "div":
        value = div(numbers)
        result = value[0]
        status = value[1] 
    elif op == "avg":
        value = avg(numbers)
        result = value[0]
        status = value[1] 
        
    else:
        status = "Unsupported operation. Please try: add 1 2, sub 2 1, mul 4 5, div 1 2 or avg 4 9"
    
    
    
    return {'value' : result, 'status' : status}

def add(operands):
    result = 0
    status = ""
    for num in operands:
        result += float(num)
    status = "Addition Successful"
    return (result, status)

    
def sub(operands):
    result = operands[0]
    status = ""
    for num in operands[1:]:
            result -= float(num)
    status = "Subtraction Successful"
    return (result, status)
    
def mul(operands):
    result = 1
    status = ""
    for num in operands:
        result *= float(num)
    status = "Multiplication Successful"
    return (result, status)
    
def div(operands):
    result = operands[0]
    status = ""
    for num in operands[1:]:
        if num != 0:
            result /= float(num)
            status = "Division Successful"
        else:
            result = 0
            status = "Error: Divide by 0"
    
    return (result, status)

def avg(operands):
    result = 0
    status = ""
    for num in operands:
        result += num
    status = "Average Successful"
    return (result/len(operands), status)

