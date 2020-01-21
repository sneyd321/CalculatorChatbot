import CogCalc as c

#result = CogCalc.main({"operator": "add", "operands": [2, 3, 5]})

#print(f"2 + 3 + 5 = {result['value']} with status {result['status']}")

#result = CogCalc.main({"operator": "avg", "operands": ["2", "3", "5"]})

#print(f"2 - 3 - 5 = {result['value']} with status {result['status']}")

#result = CogCalc.main({"operator": "mul", "operands": [2, 3, 5]})

#print(f"2 * 3 * 5 = {result['value']} with status {result['status']}")

#result = CogCalc.main({"operator": "div", "operands": [2, 3, 5]})

#print(f"2 / 3 / 5 = {result['value']} with status {result['status']}")


#c.main({"operator": "mem", "operands": ["2"]})
result = c.main({"operator": "avg", "operands": [2, 3]})
print(result)