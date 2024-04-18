from card import *

class Player:
    def __init__(self, i, hand, ai):
        self.i = int(i)
        self.hand = hand
        self.ai = ai
        self.monster = None
        self.ropa = []

    def do_cabeseo(self, table):
        """
        :returns monster_card to pick
        """
        self.monster = self.ai.pick_up_monster(table, self)
        return self.monster

    def do_turn(self, table):
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
