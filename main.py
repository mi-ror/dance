import logging
import deck
from ai_realization import *
from table import Table
import statistics
import argparse


l = logging.getLogger(__name__)


def play_game(player_nums: int):
    m_deck = deck.get_monsters_shuffled()
    [l.debug(m) for m in m_deck]
    c_deck = deck.get_cards_shuffled()
    [l.debug(m) for m in c_deck]
    l.debug('DEAL CARDS...')
    t = Table(player_nums, m_deck, c_deck, AI_T800())
    l.debug(t)
    l.debug('CABESEO...')
    t.do_cabeseo()
    l.debug(t)
    l.debug('PLAYING GAME...')
    while t.do_turn():
        pass
    l.debug(t)
    statistics.consider_game(t)


def main():
    parser = argparse.ArgumentParser(description="Simulate card game 'Dance with Monsters'.")
    parser.add_argument('--player-nums', type=int, action='store', default=6, help='count of players')
    args = parser.parse_args()

    deck.load_monster_deck()
    deck.load_card_deck()

    for _ in range(30 * 1000):
        play_game(args.player_nums)

    print('###STATISTICS###')
    statistics.print_statistics()


if __name__ == "__main__":
    main()
