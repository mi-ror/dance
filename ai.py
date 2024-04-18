import abc
from card import *

class AI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def pick_up_monster(self, table, player):
        pass

    @abc.abstractmethod
    def do_turn(self, table, player):
        pass

    def play_music(self, table, sc):
        table.music = sc.music

    def play_ropa(self, player, c):
        player.ropa.append(c)


class AI_T90(AI):
    def pick_up_monster(self, table, player):
        return table.cabeseo[0]

    def do_turn(self, table, player):
        c = player.hand.pop()
        sc = c.subcard
        if isinstance(sc, CardMusic):
            self.play_music(table, sc)
        else:
            self.play_ropa(player, c)


class AI_T500(AI):
    def pick_up_monster(self, table, player):
        return table.cabeseo[0]

    def do_turn(self, table, player):
        c_pwr = []
        m = player.monster
        for card in player.hand:
            music = table.music
            if isinstance(card.subcard, CardMusic):
                music = card.subcard.music
            pwr = m.stats[music]
            c_pwr.append((card, pwr))
        c_pwr = sorted(c_pwr, key=lambda item: item[1])
        c = c_pwr[0][0]

        player.hand.remove(c)
        sc = c.subcard
        if isinstance(sc, CardMusic):
            self.play_music(table, sc)
        else:
            self.play_ropa(player, c)


class AI_T800(AI):
    def pick_up_monster(self, table, player):
        m_pwr = []
        for m in table.cabeseo:
            for card in player.hand:
                music = table.music
                if isinstance(card.subcard, CardMusic):
                    music = card.subcard.music
                pwr = m.stats[music]
                m_pwr.append((m, pwr))
        m_pwr = sorted(m_pwr, key=lambda item: item[1], reverse=True)
        return m_pwr[0][0]

    def do_turn(self, table, player):
        c_pwr = []
        m = player.monster
        for card in player.hand:
            music = table.music
            if isinstance(card.subcard, CardMusic):
                music = card.subcard.music
            pwr = m.stats[music]
            c_pwr.append((card, pwr))
        c_pwr = sorted(c_pwr, key=lambda item: item[1])
        c = c_pwr[0][0]

        player.hand.remove(c)
        sc = c.subcard
        if isinstance(sc, CardMusic):
            self.play_music(table, sc)
        else:
            self.play_ropa(player, c)
