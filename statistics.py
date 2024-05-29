from table import Table


class MonsterStat:
    def __init__(self):
        self.games_count: int = 0
        self.games_win: int = 0
        self.place_sum: int = 0

    def win_rate(self) -> float:
        return self.games_win / self.games_count

    def place_rate(self) -> float:
        return self.place_sum / self.games_count


M_S: dict[str, MonsterStat] = {}


def consider_game(table: Table) -> None:
    global M_S
    players = table.result_table()
    players_cnt = len(players)
    for i in range(players_cnt):
        p = players[i]
        p_str = str(p.monster)
        stat = M_S.setdefault(p_str, MonsterStat())
        stat.games_count += 1
        stat.place_sum += i

    winner = players[0]
    winner_str = str(winner.monster)
    M_S[winner_str].games_win += 1


def print_statistics() -> None:
    global M_S
    for k, v in sorted(M_S.items(), key=lambda item: item[1].place_rate(), reverse=False):
        print(f'{k}: place_rate={v.place_rate():.2f} win_rate={v.win_rate():.2f} games={v.games_count} wins={v.games_win}')
