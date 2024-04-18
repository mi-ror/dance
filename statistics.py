from player import Player
from table import Table

class MonsterS:
    def __init__(self):
        self.games_count = 0
        self.games_win = 0

    def win_rate(self):
        return self.games_win / self.games_count


M_S = {}  # str(m) -> MonsterS


def consider_game(table):
    global M_S
    for p in table.players:
        p_str = str(p.monster)
        M_S.setdefault(p_str, MonsterS())
        M_S[p_str].games_count += 1
    winner = table.get_winner()
    winner_str = str(winner.monster)
    M_S[winner_str].games_win += 1


def print_statistics():
    global M_S
    for k, v in sorted(M_S.items(), key=lambda item: item[1].win_rate(), reverse=True):
        print(f'{k}: win_rate={v.win_rate()} games={v.games_count} wins={v.games_win}')