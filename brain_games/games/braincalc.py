import random
import numexpr as ne


RULES = 'What is the result of the expression?'


def generate_question_answer():
    operators = ['+', '-', '*']
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    operator = random.choice(operators)
    question = f'{num_1} {operator} {num_2}'
    result_expression = str(ne.evaluate(question))
    answer = result_expression
    return question, answer
