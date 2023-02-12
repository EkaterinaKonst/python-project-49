#!/usr/bin/env python3
from brain_games.engine import engine_game
from brain_games.games.brainprogression import progression_rules, progression_brain


def main():
    engine_game(progression_rules, progression_brain)


if __name__ == '__main__':
    main()
