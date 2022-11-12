from dataclasses import dataclass
from enum import Enum, auto
import random
from typing import Protocol


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


class EmptyDeck(Exception):
    """Empty deck Exception."""


class DeckInterface(Protocol):
    def __len__(self) -> int:
        ...

    def shuffle(self) -> None:
        ...

    def draw(self) -> Card:
        ...


class Deck:
    def __init__(self, seed: int | None = None):
        self.seed = seed
        self.random = random.Random(seed)
        self.available: list[Card] = []
        self.used: list[Card] = []
        for suite in Suite:
            for face in Face:
                self.available.append(Card(suite=suite, face=face))

    def __len__(self) -> int:
        return len(self.available)

    def shuffle(self) -> None:
        self.random.shuffle(self.available)

    def draw(self) -> Card:
        if not len(self):
            raise EmptyDeck
        card = self.available[0]
        self.available.remove(card)
        self.used.append(card)
        return card


class MultiDeck:
    def __init__(self, n: int, seed: int | None = None):
        self.decks = [Deck(seed=seed) for _ in range(n)]

    def __len__(self) -> int:
        return sum(len(deck) for deck in self.decks)

    def shuffle(self) -> None:
        for deck in self.decks:
            deck.shuffle()

    def draw(self) -> Card:
        for deck in self.decks:
            if len(deck):
                return deck.draw()
        raise EmptyDeck
