import random


RULES = 'What number is missing in the progression?'


def generate_question_answer():
    start = abs(random.randint(1, 100))
    stop = start + abs(random.randint(5, 10))
    progress_list = list(range(start, stop))
    random_index = random.randint(0, len(progress_list) - 1)
    answer = str(progress_list[random_index])
    progress_list_output = progress_list[:]
    progress_list_output[random_index] = '..'
    question = ' '.join(str(x) for x in progress_list_output)
    return question, answer
