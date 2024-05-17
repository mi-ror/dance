from ai import AI
from card import Card
from monster import Monster
from player import Player


class Table:
    def __init__(self, p_count: int, m_deck: list[Monster], c_deck: list[Card], ai: AI):
        self._c_deck: list[Card] = c_deck

        self.players: list[Player] = []
        self.player_last_turn: list[int] = []
        for i in range(p_count):
            hand = []
            for _ in range(4):
                hand.append(c_deck.pop())
            p = Player(i, hand, ai)
            self.players.append(p)
            self.player_last_turn.append(-1)
        self._cur_i: int = 0
        self.pass_count: int = 0

        self.cabeseo: list[Monster] = []
        for _ in range(len(self.players) + 0):
            self.cabeseo.append(m_deck.pop())

        self.music: int = 0

    def cur_i(self) -> int:
        return self._cur_i % len(self.players)

    def __str__(self):
        return 'CABESEO: ' + '\n\t' \
               + '\n\t'.join(str(p) for p in self.cabeseo) \
               + f'\nMUSIC: {self.music}'\
               + '\nCUR: ' + str(self.cur_i()) + '(' + str(self.pass_count) + ')\n\t' \
               + '\n\t'.join(str(p) for p in self.players)

    def do_cabeseo(self) -> None:
        for p in self.players:
            picked_m = p.do_cabeseo(self)
            self.cabeseo.remove(picked_m)

    def do_turn(self) -> None:
        i = self.cur_i()
        if self.players[i].do_turn(self):
            self.player_last_turn[i] = self._cur_i
        else:
            self.pass_count += 1
        self._cur_i += 1
        return self.pass_count < len(self.players)

    def get_winner(self) -> Player:
        winner_i = 0
        winner_pwr = -100
        for i in range(len(self.players)):
            pwr = self.player_power(i)
            if pwr > winner_pwr or (pwr == winner_pwr and self.player_last_turn[i] < self.player_last_turn[winner_i]):
                winner_i = i
                winner_pwr = pwr
        return self.players[winner_i]

    def player_power(self, i) -> int:
        p = self.players[i]
        return p.monster.stats[self.music]