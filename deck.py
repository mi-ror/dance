from monster import Monster
from card import *
import json
import random

MONSTER_DECK = []
CARD_DECK = []


def _load_monster_deck():
    global MONSTER_DECK
    MONSTER_DECK = []
    with open('monsters.json') as mf:
        data = json.load(mf)
    for e in data:
        m = Monster(e['stats'])
        MONSTER_DECK.append(m)

def get_monsters_shuffled():
    res = MONSTER_DECK.copy()
    random.shuffle(res)
    return res


def _load_card_deck():
    global CARD_DECK
    CARD_DECK = []
    with open('cards.json') as mf:
        data = json.load(mf)
    for e in data:
        type = e['type']
        if type == 'stub':
            subcard = None
        elif type == 'music':
            subcard = CardMusic(e['music'])
        else:
            raise Exception(f'unknown card type: {type}')
        m = Card(subcard)
        CARD_DECK.append(m)
    return CARD_DECK


def get_cards_shuffled():
    res = CARD_DECK.copy()
    random.shuffle(res)
    return res


_load_monster_deck()
_load_card_deck()
