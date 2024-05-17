import abc
from card import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from monster import Monster
    from player import Player
    from table import Table


class AI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def pick_up_monster(self, table: 'Table', player: 'Player') -> 'Monster':
        pass

    @abc.abstractmethod
    def do_turn(self, table: 'Table', player: 'Player') -> None:
        pass

    def play_music(self, table: 'Table', sc: 'SubCard') -> None:
        table.music = sc.music

    def play_ropa(self, player: 'Player', c: 'Card') -> None:
        player.ropa.append(c)


