from ai import AI
from card import *
from monster import Monster
from player import Player
from table import Table


def _play_music(table: Table, sc_music: CardMusic) -> None:
    table.music = sc_music.music


def _play_ropa(player: Player, c: Card) -> None:
    player.ropa.append(c)


def _do_optimal_turn(table: Table, player: Player) -> None:
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
        _play_music(table, sc)
    else:
        _play_ropa(player, c)


class AI_T90(AI):
    def pick_up_monster(self, table: Table, player: Player) -> Monster:
        return table.cabeseo[0]

    def do_turn(self, table: Table, player: Player) -> None:
        c = player.hand.pop()
        sc = c.subcard
        if isinstance(sc, CardMusic):
            _play_music(table, sc)
        else:
            _play_ropa(player, c)


class AI_T500(AI):
    def pick_up_monster(self, table: Table, player: Player) -> Monster:
        return table.cabeseo[0]

    def do_turn(self, table: Table, player: Player) -> None:
        _do_optimal_turn(table, player)


class AI_T800(AI):
    def pick_up_monster(self, table: Table, player: Player) -> Monster:
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

    def do_turn(self, table: Table, player: Player) -> None:
        _do_optimal_turn(table, player)
