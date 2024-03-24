import random
import time


OPERATORS = [ '+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12

TOTAL_QUESTION = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + ' ' + operator + ' ' + str(right)
    print(expr)
    answer = eval(expr)
    return expr , answer

input("press enter to start")
start_time = time.time()
for i in range(TOTAL_QUESTION):
    question, answer = generate_problem()
    
    answer1 = input("enter the answer = " )

    if str(answer) == answer1:
        print(f"correct answer ")
    else:
        print('wrong answer')
        print(f"answer of {question} = {answer}")

end_time = time.time()
total_time = round(start_time - end_time)

print(f" total Time taken  =  {total_time} sec")