#!/usr/bin/env python3
import random


def prime_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def primebrain():
    res_list = []
    num = random.randint(1, 100)
    res_list.append(num)
    count = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count += 1
    if count <= 0:
        res_list.append('yes')
    else:
        res_list.append('no')
    return res_list
