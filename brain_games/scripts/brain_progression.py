from brain_games.engine import run
from brain_games.games.brainprogression import RULES, generate_question_answer


def main():
    run(RULES, generate_question_answer)


if __name__ == '__main__':
    main()
