# Card games

Games involving decks of cards.

## Getting started

You'll need Python 3.10+, otherwise, just install from GitHub and get going!

```shell
path/to/python -m pip install "git+https://github.com/samthorold/deck-of-cards-python.git"
```

Deck of cards.

```python
from card_games.deck import Deck, MultiDeck()
deck = Deck()
deck.shuffle()
deck.draw()
```

