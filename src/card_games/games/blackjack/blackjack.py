"""
N players.

House is a player, but with rules governing actions.

A player's turn may involve 1+ draws and they are either free to "stick" or
"twist" or are "bust" after each draw.


"""


import itertools
import random
from typing import Protocol

from card_games.deck import Card, DeckInterface, Face, MultiDeck


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


class Hand:
    def __init__(self, cards: list[Card] | None = None):
        self.cards: list[Card] = [] if cards is None else cards

    def __len__(self):
        return len(self.cards)

    @property
    def values(self) -> list[int]:
        value_permutations = itertools.product(
            *[[value for value in card_values(card)] for card in self.cards]
        )
        return [sum(permutation) for permutation in value_permutations]

    def add(self, card: Card) -> None:
        self.cards.append(card)


class PlayerInterface(Protocol):

    name: str
    hand: Hand

    def action(self, deck: DeckInterface) -> bool:
        ...

    def new_hand(self) -> None:
        ...


class AbstractPlayer:
    def __init__(self, name: str, hand: Hand | None = None):
        self.name = name
        self.hand = Hand() if hand is None else hand

    def new_hand(self) -> None:
        self.hand = Hand()

    def action(self, deck: DeckInterface) -> bool:
        raise NotImplemented


class House(AbstractPlayer):
    def action(self, deck: DeckInterface) -> bool:
        """If the hand value is >= 16, stick, otherwise twist."""
        if any(v < 16 for v in self.hand.values):
            self.hand.add(deck.draw())
            return True
        return False


class RandomPlayer(AbstractPlayer):
    def __init__(self, name: str, hand: Hand | None = None, seed: int | None = None):
        super().__init__(name=name, hand=hand)
        self.random = random.Random(seed)

    def action(self, deck: DeckInterface) -> bool:
        """Take first card then 50/50 chance of stick or twist."""
        if not len(self.hand) or self.random.randint(0, 1):
            self.hand.add(deck.draw())
            return True
        return False


class Game:
    def __init__(
        self,
        players: list[PlayerInterface],
        deck: DeckInterface | None = None,
        seed: int | None = None,
    ):
        self.house = House("House")
        self.players = players
        self.in_play = [p for p in self.players]
        self.deck = MultiDeck(4, seed) if deck is None else deck

    def is_bust(self, player: PlayerInterface) -> bool:
        if all(v > 21 for v in player.hand.values):
            return True
        return False

    def player_turn(self, player: PlayerInterface) -> None:
        player.new_hand()
        while True:  # only so many cards in the deck so reckon we are safe
            ask_again = player.action(self.deck)
            print(player.name, player.hand.values)
            if self.is_bust(player):
                print(player.name, "bust")
                if player is not self.house:
                    self.in_play.remove(player)
                break
            if not ask_again:
                break

    def game_turn(self) -> None:
        self.in_play = [p for p in self.players]
        for player in self.in_play:
            self.player_turn(player)
        self.player_turn(self.house)
        if self.is_bust(self.house):
            for player in self.in_play:
                print(player.name, "wins")
            return
        house_score = max(self.house.hand.values)
        for player in self.in_play:
            if any(v > house_score for v in player.hand.values):
                print(player.name, "wins")
            else:
                print(player.name, "the house wins :)")
