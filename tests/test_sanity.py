from card_games.deck import Card, Deck, Face, Suite


def test_sanity():
    deck = Deck(seed=1)
    exp = [
        Card(suite=Suite.CLUB, face=Face.TWO),
        Card(suite=Suite.CLUB, face=Face.FIVE),
    ]
    got = [deck.draw()]
    deck.shuffle()
    got.append(deck.draw())
    assert got == exp
