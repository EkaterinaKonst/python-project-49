#!/usr/bin/env python3
import prompt
import random
from ..engine import *


def rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')

def evenbrain():
    res_list = []
    num = random.randint(1, 100)
    res_list.append(num)
    if num % 2 == 0:
        res_list.append('yes')
    else:
        res_list.append('no')
    return res_list


def main():
    engine_game(evenbrain)


if __name__ == '__main__':
    main()
