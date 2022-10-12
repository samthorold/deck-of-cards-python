import pytest

from card_games.deck import Card, Deck, EmptyDeck, MultiDeck, Face, Suite


@pytest.mark.parametrize("deck", (Deck(seed=1), MultiDeck(n=2, seed=1)))
def test_sanity(deck):
    exp = [
        Card(suite=Suite.CLUB, face=Face.TWO),
        Card(suite=Suite.CLUB, face=Face.FIVE),
    ]
    got = [deck.draw()]
    deck.shuffle()
    got.append(deck.draw())
    assert got == exp


@pytest.mark.parametrize("deck", (Deck(seed=1), MultiDeck(n=2, seed=1)))
def test_empty_deck(deck):
    with pytest.raises(EmptyDeck):
        for _ in range(300):
            deck.draw()


@pytest.mark.parametrize(
    "deck,length", ((Deck(seed=1), 52), (MultiDeck(n=2, seed=1), 104))
)
def test_len(deck, length):
    assert len(deck) == length
