#!/usr/bin/env python3
from brain_games.engine import engine_game
from brain_games.games.braincalc import calcbrain, calcbrain_rules


def main():
    engine_game(calcbrain_rules, calcbrain)


if __name__ == '__main__':
    main()
