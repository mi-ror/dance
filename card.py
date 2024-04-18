class Card:
    def __init__(self, subcard):
        """
        subcard - класс, который реализует один из типов карты
        """
        self.subcard = subcard

    def __str__(self):
        return 'Card: {' + str(self.subcard) + '}'


class CardMusic:
    def __init__(self, music):
        self.music = int(music)

    def __str__(self):
        return 'music: ' + str(self.music)
