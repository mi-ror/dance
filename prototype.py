import random

class Monster:
    def __init__(self, stats):
        self.stats = stats

    def get_stat(self, music):
        return self.stats[music - 1]

class Card:
    def __init__(self, bonus):
        self.bonus = bonus

class Player:
    def __init__(self, player_id, monster, cards):
        self.player_id = player_id
        self.monster = monster
        self.cards = cards
        self.score = 0

    def play_card(self):
        if self.cards:
            card = self.cards.pop(0)
            self.score += card.bonus
            print(f"Player {self.player_id} played a card. Bonus: {card.bonus}. Total score: {self.score}")
        else:
            print(f"Player {self.player_id} has no more cards.")


def create_deck():
    deck = []
    for _ in range(20):  
        bonus = random.randint(1, 3) 
        deck.append(Card(bonus))
    random.shuffle(deck)
    return deck


def create_monster():
    stats = [random.randint(1, 8) for _ in range(4)]  #
    return Monster(stats)


def play_game():
    music = random.randint(1, 4)  
    print("Chosen music number:", music)
    
    monsters = [create_monster() for _ in range(4)]
    print("Monster Stats:")
    for i, monster in enumerate(monsters, 1):
        print(f"Monster {i}: {monster.stats}")

    players = []
    for i in range(1, 5):
        monster = monsters[i - 1]
        deck = create_deck()
        player = Player(i, monster, deck[:4])
        players.append(player)
    
    for i, player in enumerate(players):
        print(f"\nPlayer {player.player_id}:")
        for j, card in enumerate(player.cards):
            print(f"Card {j + 1}: Bonus = {card.bonus}")
    
    num_cards_played = 0
    while any(player.cards for player in players):
        print("\nStarting a new round...")
        for player in players:
            if player.cards:
                player.play_card()
                num_cards_played += 1
                if num_cards_played == 4:
                    num_cards_played = 0
    
    print("\nAdding monster bonuses to final scores...")
    for player in players:
        player.score += player.monster.get_stat(music)
        print(f"Player {player.player_id}'s final score (including monster's bonus): {player.score}")

    print("\nFinal scores:")
    for player in players:
        print(f"Player {player.player_id}: {player.score}")
    
    winner = max(players, key=lambda x: x.score)
    print(f"\nPlayer {winner.player_id} wins with {winner.score} points!")


play_game()
