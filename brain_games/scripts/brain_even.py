#!/usr/bin/env python3
import prompt
import random


def evenbrain():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 3
    count_list = []
    while count != 0:
        num = random.randint(1,100)
        print(f'Question: {num}')
        ans = prompt.string('Your answer: ')
        if num % 2 == 0 and ans == 'yes':
            count_list.append(ans)
            print('Correct!')
        elif num % 2 != 0 and ans == 'no':
            count_list.append(ans)
            print('Correct!')
        elif num % 2 == 0 and ans == 'no':
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}")
            break
        elif num % 2 != 0 and ans == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}")
            break
        else:
            print(f"{ans} is wrong answer ;(.")
            print(f"Let's try again, {name}")
            break
        count -= 1
        if len(count_list) == 3:
            print(f"Congratulations, {name}")


def main():
    evenbrain()


if __name__ == '__main__':
    main()
