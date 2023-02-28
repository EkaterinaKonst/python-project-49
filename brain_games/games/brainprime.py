import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


def generate_question_answer():
    question = random.randint(1, 100)
    prime_check = is_prime(question)
    answer = None
    if prime_check is True:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
