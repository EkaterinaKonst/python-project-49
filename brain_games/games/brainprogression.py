#!/usr/bin/env python3
import random


def progression_rules():
    print('What number is missing in the progression?')

def progression_brain():
    res_list = []
    start = abs(random.randint(1, 100))
    stop = start + abs(random.randint(7, 10))
    step = abs(random.randint(1, 2))
    progress_list = list(range(start, stop, step))
    random_index = random.randint(0, len(progress_list)-1)
    correct_answer = str(progress_list[random_index])
    progress_list_output = progress_list[:]
    progress_list_output[random_index] = '..'
    string_output = ' '.join(str(x) for x in progress_list_output)
    res_list.append(string_output)
    res_list.append(correct_answer)
    return res_list

