from ai import AI
from card import *
from monster import Monster


class Player:
    def __init__(self, i: int, hand: list[Card], ai: AI):
        self.i: int = i
        self.hand: list[Card] = hand
        self.ai: AI = ai
        self.monster: Monster | None = None
        self.ropa: list[Card] = []

    def do_cabeseo(self, table) -> Monster:
        """
        :returns monster_card to pick
        """
        self.monster = self.ai.pick_up_monster(table, self)
        return self.monster

    def do_turn(self, table) -> bool:
        if not self.hand:
            return False

        self.ai.do_turn(table, self)
        c = self.hand.pop()
        sc = c.subcard
        if isinstance(sc, CardMusic):
            table.music = sc.music
        else:
            self.ropa.append(c)
        return True

    def __str__(self):
        return str(self.i) + ': ' + str(self.monster)\
               + ' [' + ','.join(str(c) for c in self.hand) + ']'\
               + '@{' + ','.join(str(c) for c in self.ropa) + '}'
