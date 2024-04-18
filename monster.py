class Monster:
    def __init__(self, stats):
        """
        id - uniq id
        stats - [T, V, M, N] of int
        """
        self.id = id
        self.stats = stats
        for i in range(len(self.stats)):
            self.stats[i] = int(self.stats[i])

    def get_stat(self, music):
        return self.stats[music - 1]

    def __str__(self):
        return '[' + ', '.join(str(x) for x in self.stats) + ']'
