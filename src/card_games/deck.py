"""Classic deck."""

from dataclasses import dataclass
from enum import Enum, auto
import random
from typing import Protocol


class Suite(Enum):
    """Card suite."""

    CLUB = auto()
    DIAMOND = auto()
    HEART = auto()
    SPADE = auto()


class Face(Enum):
    """Card face."""

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
    """Card from a classic deck.

    Attributes:
        suite (Suite): Card suite; Club, Diamond, Heart, or Spade.
        face (Face): Card face.
    """

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
    """Classic deck of cards.

    Examples:
        >>> deck = Deck(seed=1)
        >>> deck.shuffle()
        >>> deck.draw()
        Card(suite=<Suite.SPADE: 4>, face=<Face.QUEEN: 11>)

    Attributes:
        seed (int): Random seed.
        n (int): Number of decks to include.

    """

    def __init__(self, seed: int | None = None, n: int = 1):
        self.seed = seed
        self.n = n
        self.random = random.Random(seed)
        self.available: list[Card] = []
        self.used: list[Card] = []
        for _ in range(n):
            for suite in Suite:
                for face in Face:
                    self.available.append(Card(suite=suite, face=face))

    def __len__(self) -> int:
        return len(self.available)

    def shuffle(self) -> None:
        self.random.shuffle(self.available)

    def draw(self) -> Card:
        """Draw a [card][card_games.deck.Card].

        Returns:
            card: Single [Card][card_games.deck.Card] object.

        Raises:
            EmptyDeck: If there are no cards left, raise and error.
        """
        if not len(self):
            raise EmptyDeck
        card = self.available[0]
        self.available.remove(card)
        self.used.append(card)
        return card
