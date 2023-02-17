#!/usr/bin/env python3
import random


def gcd_brain_rules():
    print('Find the greatest common divisor of given numbers.')


def gcd_brain():
    res_list = []
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    res_list.append(f'{num_1} {num_2}')
    while num_1 != 0 and num_2 != 0:
        if num_1 >= num_2:
            num_1 %= num_2
        else:
            num_2 %= num_1
    res_list.append(str(num_1 or num_2))
    return res_list
