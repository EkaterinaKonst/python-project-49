#!/usr/bin/env python3
import prompt


def greeting():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def engine_game(rules, func):
    trials = 3
    count_victory = 0
    print('Welcome to the Brain Games!')
    name_and_greeting = greeting()
    rules()
    while trials != 0:
        result = func()
        print(f'Question: {result[0]}')
        answer = prompt.string('Your answer: ')
        if answer == result[1]:
            count_victory += 1
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{result[1]}".')
            print(f"Let's try again, {name_and_greeting }")
            break
        trials -= 1
    if count_victory == 3:
        print(f"Congratulations, {name_and_greeting}!")
