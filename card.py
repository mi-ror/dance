class SubCard:
    pass


class Card:
    def __init__(self, subcard: SubCard):
        """
        subcard - класс, который реализует один из типов карты
        """
        self.subcard: SubCard = subcard

    def __str__(self):
        return 'Card: {' + str(self.subcard) + '}'


class CardMusic(SubCard):
    def __init__(self, music: int):
        assert 0 <= music and music <= 3, f"Wrong music: {music}"
        self.music: int = music

    def __str__(self):
        return 'music: ' + str(self.music)
