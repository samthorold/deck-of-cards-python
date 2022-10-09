from dataclasses import dataclass
from enum import Enum, auto
from pickle import NONE
import random


class Suite(Enum):
    CLUB = auto()
    DIAMOND = auto()
    HEART = auto()
    SPADE = auto()


class Face(Enum):
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()


@dataclass(frozen=True)
class Card:
    suite: Suite
    face: Face


class Deck:
    def __init__(self, seed: int | None = None):
        self.seed = seed
        self.random = random.Random(seed)
        self.available: list[Card] = []
        self.used: list[Card] = []
        for suite in Suite:
            for face in Face:
                self.available.append(Card(suite=suite, face=face))

    def shuffle(self):
        self.random.shuffle(self.available)

    def draw(self):
        card = self.available[0]
        self.available.remove(card)
        self.used.append(card)
        return card


if __name__ == "__main__":
    print("Deck of cards")
    deck = Deck()
    print(deck.draw())
    deck.shuffle()
    print(deck.draw())
