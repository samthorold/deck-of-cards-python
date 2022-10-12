"""
N players.

House is a player, but with rules governing actions.

A player's turn may involve 1+ draws and they are either free to "stick" or
"twist" or are "bust" after each draw.


"""


from dataclasses import dataclass
import itertools

from card_games.deck import Card, Face


def card_values(card: Card) -> list[int]:
    if card.face == Face.TWO:
        return [2]
    if card.face == Face.THREE:
        return [3]
    if card.face == Face.FOUR:
        return [4]
    if card.face == Face.FIVE:
        return [5]
    if card.face == Face.SIX:
        return [6]
    if card.face == Face.SEVEN:
        return [7]
    if card.face == Face.EIGHT:
        return [8]
    if card.face == Face.NINE:
        return [9]
    if card.face == Face.TEN:
        return [10]
    if card.face == Face.JACK:
        return [10]
    if card.face == Face.QUEEN:
        return [10]
    if card.face == Face.KING:
        return [10]
    if card.face == Face.ACE:
        return [1, 11]
    raise ValueError(f"Unknown card face value {card.face}")


@dataclass
class Hand:
    cards: list[Card]

    @property
    def values(self) -> list[int]:
        value_permutations = itertools.product(
            *[[value for value in card_values(card)] for card in self.cards]
        )
        return [sum(permutation) for permutation in value_permutations]


@dataclass
class Player:
    name: str
    hand: Hand
