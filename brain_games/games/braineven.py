import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    question = random.randint(1, 100)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
