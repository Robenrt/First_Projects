import random

operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12
total_problems = 10

def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expr = f"{left} {operator} {right}"
    print(expr)
    return expr

generate_problem()

for i in range(total_problems):
    ...
