from ai import AI
from card import Card
from monster import Monster
from player import Player


class _PlayerExt:
    def __init__(self, p: Player, power: int, last_turn: int):
        self.player: Player = p
        self.power: int = power
        self.last_turn: int = last_turn

    def __eq__(self, other: '_PlayerExt'):
        return (self.power, self.last_turn) == (other.power, other.last_turn)

    def __lt__(self, other: '_PlayerExt'):
        if self.power < other.power:
            return True
        if self.power > other.power:
            return False
        if self.last_turn > other.last_turn:
            return True
        return False


class Table:
    def __init__(self, p_count: int, m_deck: list[Monster], c_deck: list[Card], ai: AI):
        self._c_deck: list[Card] = c_deck

        self._players: list[Player] = []
        self._player_last_turn: list[int] = []
        for i in range(p_count):
            hand = []
            for _ in range(6):
                hand.append(c_deck.pop())
            p = Player(i, hand, ai)
            self._players.append(p)
            self._player_last_turn.append(-1)
        self._cur_i: int = 0
        self._pass_count: int = 0

        self.cabeseo: list[Monster] = []
        for _ in range(len(self._players) + 0):
            self.cabeseo.append(m_deck.pop())

        self.music: int = 0

    def cur_i(self) -> int:
        return self._cur_i % len(self._players)

    def __str__(self):
        return 'CABESEO: ' + '\n\t' \
               + '\n\t'.join(str(p) for p in self.cabeseo) \
               + f'\nMUSIC: {self.music}' \
               + '\nCUR: ' + str(self.cur_i()) + '(' + str(self._pass_count) + ')\n\t' \
               + '\n\t'.join(str(p) for p in self._players)

    def do_cabeseo(self) -> None:
        for p in self._players:
            picked_m = p.do_cabeseo(self)
            self.cabeseo.remove(picked_m)

    def do_turn(self) -> bool:
        i = self.cur_i()
        if self._players[i].do_turn(self):
            self._player_last_turn[i] = self._cur_i
        else:
            self._pass_count += 1
        self._cur_i += 1
        return self._pass_count < len(self._players)

    def result_table(self) -> list[Player]:
        """
        :returns Players table sorted by place
        """
        players_ext: list[_PlayerExt] = []
        for i in range(len(self._players)):
            p_ext = _PlayerExt(self._players[i], self.player_power(i), self._player_last_turn[i])
            players_ext.append(p_ext)

        result: list[Player] = [p_ext.player for p_ext in sorted(players_ext, reverse=True)]
        return result

    def player_power(self, i) -> int:
        p = self._players[i]
        return p.monster.stats[self.music]
