import deck
from table import Table
import statistics


def play_game():
    m_deck = deck.get_monsters_shuffled()
    # [print(m) for m in m_deck]
    c_deck = deck.get_cards_shuffled()
    # [print(m) for m in c_deck]
    # print('DEAL CARDS...')
    t = Table(4, m_deck, c_deck)
    # print(t)
    # print('CABESEO...')
    t.do_cabeseo()
    # print(t)
    # print('PLAYING GAME...')
    while t.do_turn():
        pass
    # print(t)
    statistics.consider_game(t)


def main():
    for _ in range(30 * 1000):
        play_game()
    print('###STATISTICS###')
    statistics.print_statistics()


if __name__ == "__main__":
    main()