class Monster:
    def __init__(self, stats: list[int]):
        """
        stats - [T, V, M, N] of int
        """
        assert len(stats) == 4, f"wrong stats: {*stats,}"
        self.stats: list[int] = stats

    def get_stat(self, music: int) -> int:
        return self.stats[music - 1]

    def __str__(self):
        return '[' + ', '.join(str(x) for x in self.stats) + ']'
