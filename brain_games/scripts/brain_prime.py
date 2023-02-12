#!/usr/bin/env python3
from brain_games.engine import engine_game
from brain_games.games.brainprime import prime_rules, primebrain


def main():
    engine_game(prime_rules, primebrain)


if __name__ == '__main__':
    main()
