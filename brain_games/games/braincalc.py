#!/usr/bin/env python3
import random
import numexpr as ne


def calcbrain_rules():
    print('What is the result of the expression?')


def calcbrain():
    res_list = []
    operators = ['+', '-', '*']
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    operator = random.choice(operators)
    res_list.append(f'{num_1} {operator} {num_2}')
    expression = res_list[0]
    result_expression = str(ne.evaluate(expression))
    res_list.append(result_expression)
    return res_list
