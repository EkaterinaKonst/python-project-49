#!/usr/bin/env python3
from brain_games.engine import engine_game
from brain_games.games.braingsd import gsd_brain, gsd_brain_rules


def main():
    engine_game(gsd_brain_rules, gsd_brain)


if __name__ == '__main__':
    main()
