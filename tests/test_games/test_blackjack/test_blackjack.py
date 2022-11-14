import pytest

from card_games.deck import Card, Face, Suite
from card_games.games.blackjack.blackjack import card_values, Hand


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
def test_hand_values(hand: Hand, value: list[int]) -> None:
    assert hand.values == value


def test_all_face_values_have_a_numeric_value() -> None:
    for face in Face:
        card_values(Card(Suite.HEART, face))


def test_hand_has_length() -> None:
    assert len(Hand()) == 0
    assert len(Hand([Card(Suite.CLUB, Face.FIVE), Card(Suite.CLUB, Face.FIVE)])) == 2
