from monster import Monster
from card import *
import json
import random

MONSTER_DECK: list[Monster] = []
CARD_DECK: list[Card] = []


def load_monster_deck() -> None:
    global MONSTER_DECK
    MONSTER_DECK = []
    with open('monsters.json') as mf:
        data = json.load(mf)
    for e in data:
        m = Monster(e['stats'])
        MONSTER_DECK.append(m)


def get_monsters_shuffled() -> list[Monster]:
    res = MONSTER_DECK.copy()
    random.shuffle(res)
    return res


def load_card_deck() -> list[Card]:
    global CARD_DECK
    CARD_DECK = []
    with open('cards.json') as mf:
        data = json.load(mf)
    for e in data:
        card_type = e['type']
        if card_type == 'stub':
            subcard = None
        elif card_type == 'music':
            subcard = CardMusic(e['music'])
        else:
            raise Exception(f'unknown card type: {card_type}')
        m = Card(subcard)
        CARD_DECK.append(m)
    return CARD_DECK


def get_cards_shuffled() -> list[Card]:
    res = CARD_DECK.copy()
    random.shuffle(res)
    return res


# load_monster_deck()
# load_card_deck()
