import prompt

TRIALS = 3


def greeting():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run(rules, func):
    count_trials = 0
    count_victory = 0
    print('Welcome to the Brain Games!')
    name_and_greeting = greeting()
    print(rules)
    while count_trials != TRIALS:
        result = func()
        print(f'Question: {result[0]}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == result[1]:
            count_victory += 1
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(. ', end='')
            print(f'Correct answer was "{result[1]}".')
            print(f"Let's try again, {name_and_greeting }!")
            break
        count_trials += 1
    if count_victory == 3:
        print(f"Congratulations, {name_and_greeting}!")
