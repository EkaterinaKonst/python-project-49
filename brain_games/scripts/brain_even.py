#!/usr/bin/env python3
from brain_games.engine import engine_game
from brain_games.games.braineven import evenbrain, evenbrain_rules


def main():
    engine_game(evenbrain_rules, evenbrain)


if __name__ == '__main__':
    main()
