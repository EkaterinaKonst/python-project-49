import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return 'no'
    return 'yes'


def generate_question_answer():
    question = random.randint(1, 100)
    count = 0
    answer = is_prime(question)
    return question, answer
