from player import Player
from ai import *

class Table:
    def __init__(self, p_count, m_deck, c_deck):
        self._m_deck = m_deck
        self._c_deck = c_deck

        self.players = []
        self.player_last_turn = []
        for i in range(p_count):
            hand = []
            for _ in range(4):
                hand.append(c_deck.pop())
            p = Player(i, hand, AI_T800())
            self.players.append(p)
            self.player_last_turn.append(-1)
        self._cur_i = 0
        self.pass_count = 0

        self.cabeseo = []
        for _ in range(len(self.players) + 2):
            self.cabeseo.append(m_deck.pop())

        self.music = 0

    def cur_i(self):
        return self._cur_i % len(self.players)

    def __str__(self):
        return 'CABESEO: ' + '\n\t' \
               + '\n\t'.join(str(p) for p in self.cabeseo) \
               + f'\nMUSIC: {self.music}'\
               + '\nCUR: ' + str(self.cur_i()) + '(' + str(self.pass_count) + ')\n\t' \
               + '\n\t'.join(str(p) for p in self.players)

    def do_cabeseo(self):
        for p in self.players:
            picked_m = p.do_cabeseo(self)
            self.cabeseo.remove(picked_m)

    def do_turn(self):
        i = self.cur_i()
        if self.players[i].do_turn(self):
            self.player_last_turn[i] = self._cur_i
        else:
            self.pass_count += 1
        self._cur_i += 1
        return self.pass_count < len(self.players)

    def get_winner(self):
        winner_i = 0
        winner_pwr = -100
        for i in range(len(self.players)):
            pwr = self.player_power(i)
            if pwr > winner_pwr or (pwr == winner_pwr and self.player_last_turn[i] < self.player_last_turn[winner_i]):
                winner_i = i
                winner_pwr = pwr
        # if str(self.players[winner_i].monster) == '[1, 5, 7, 9]':
        #     print(self)
        #     pass
        return self.players[winner_i]

    def player_power(self, i):
        p = self.players[i]
        return p.monster.stats[self.music]