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

deck = MultiDeck(4)
deck.shuffle()
deck.draw()
```

Blackjack.

```python
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
```