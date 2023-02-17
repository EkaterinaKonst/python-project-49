#!/usr/bin/env python3
from brain_games.engine import engine_game
from brain_games.games.braingcd import gcd_brain, gcd_brain_rules


def main():
    engine_game(gcd_brain_rules, gcd_brain)


if __name__ == '__main__':
    main()
