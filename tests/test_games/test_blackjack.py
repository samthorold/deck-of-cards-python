import pytest

from card_games.deck import Card, Face, Suite
from card_games.games.blackjack.blackjack import Hand


@pytest.mark.parametrize(
    "hand,value",
    (
        (
            Hand(
                cards=[
                    Card(suite=Suite.CLUB, face=Face.TWO),
                    Card(suite=Suite.CLUB, face=Face.FIVE),
                ]
            ),
            [7],
        ),
        (
            Hand(
                cards=[
                    Card(suite=Suite.CLUB, face=Face.TWO),
                    Card(suite=Suite.CLUB, face=Face.ACE),
                ]
            ),
            [3, 13],
        ),
    ),
)
def test_hand_values(hand: Hand, value: list[int]):
    assert hand.values == value
