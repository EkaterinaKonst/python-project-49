import random
import math


RULES = 'Find the greatest common divisor of given numbers.'


def generate_question_answer():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    question = f'{num_1} {num_2}'
    answer = str(math.gcd(num_1, num_2))
    return question, answer
