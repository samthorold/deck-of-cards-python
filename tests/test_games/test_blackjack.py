import pytest

from card_games.deck import Card, Face, Suite, MultiDeck
from card_games.games.blackjack.blackjack import card_values, Hand, Game, RandomPlayer


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


def test_all_face_values_have_a_numeric_value():
    for face in Face:
        card_values(Card(Suite.HEART, face))


def test_unknown_face_value():
    with pytest.raises(ValueError):
        card_values(Card(Suite.HEART, "barnacles"))


def test_game():
    # Player 1 > House
    deck = MultiDeck(4, seed=2)
    deck.shuffle()
    players = [RandomPlayer("Player 1", seed=5)]
    game = Game(players, deck, seed=1)
    game.game_turn()

    # Both bust
    deck = MultiDeck(4, seed=1)
    deck.shuffle()
    players = [RandomPlayer("Player 1", seed=5)]
    game = Game(players, deck, seed=1)
    game.game_turn()

    # House > Player 1
    deck = MultiDeck(4, seed=1)
    deck.shuffle()
    players = [RandomPlayer("Player 1", seed=1)]
    game = Game(players, deck, seed=1)
    game.game_turn()

    # House bust
    deck = MultiDeck(4, seed=10)
    deck.shuffle()
    players = [RandomPlayer("Player 1", seed=1)]
    game = Game(players, deck, seed=1)
    game.game_turn()
