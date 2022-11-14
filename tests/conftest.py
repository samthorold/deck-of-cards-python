import pytest

from card_games.deck import Card, DeckInterface, Face, Suite
from card_games.games.blackjack.blackjack import AbstractPlayer


class TensDeck:
    def __init__(self) -> None:
        self.cards = [
            Card(Suite.CLUB, Face.TEN),
            Card(Suite.DIAMOND, Face.TEN),
            Card(Suite.HEART, Face.TEN),
            Card(Suite.SPADE, Face.TEN),
            Card(Suite.CLUB, Face.JACK),
        ]

    def __len__(self) -> int:
        return len(self.cards)

    def shuffle(self) -> None:
        pass

    def draw(self) -> Card:
        card = self.cards[0]
        self.cards = self.cards[1:]
        return card


@pytest.fixture
def tens_deck() -> TensDeck:
    return TensDeck()


class TensThenNinesDeck:
    def __init__(self) -> None:
        self.cards = [
            Card(Suite.CLUB, Face.TEN),
            Card(Suite.DIAMOND, Face.TEN),
            Card(Suite.HEART, Face.NINE),
            Card(Suite.SPADE, Face.NINE),
        ]

    def __len__(self) -> int:
        return len(self.cards)

    def shuffle(self) -> None:
        pass

    def draw(self) -> Card:
        card = self.cards[0]
        self.cards = self.cards[1:]
        return card


@pytest.fixture
def tens_then_nines_deck() -> TensThenNinesDeck:
    return TensThenNinesDeck()


class FifteenThenTenDeck:
    def __init__(self) -> None:
        self.cards = [
            Card(Suite.CLUB, Face.TEN),
            Card(Suite.DIAMOND, Face.TEN),
            Card(Suite.HEART, Face.FIVE),
            Card(Suite.SPADE, Face.TEN),
        ]

    def __len__(self) -> int:
        return len(self.cards)

    def shuffle(self) -> None:
        pass

    def draw(self) -> Card:
        card = self.cards[0]
        self.cards = self.cards[1:]
        return card


@pytest.fixture
def fifteen_then_ten_deck() -> FifteenThenTenDeck:
    return FifteenThenTenDeck()


class AlwaysTwistPlayer(AbstractPlayer):
    def __init__(self, name: str = "Always Twist"):
        super().__init__(name)

    def action(self, deck: DeckInterface) -> bool:
        self.hand.add(deck.draw())
        return True


@pytest.fixture
def always_twist_player() -> AlwaysTwistPlayer:
    return AlwaysTwistPlayer()


class NeverTwistPlayer(AbstractPlayer):
    def __init__(self, name: str = "Never Twist"):
        super().__init__(name)

    def action(self, deck: DeckInterface) -> bool:
        self.hand.add(deck.draw())
        return False


@pytest.fixture
def never_twist_player() -> NeverTwistPlayer:
    return NeverTwistPlayer()


class OneTwistPlayer(AbstractPlayer):
    def __init__(self, name: str = "One Twist"):
        super().__init__(name)

    def action(self, deck: DeckInterface) -> bool:
        self.hand.add(deck.draw())
        if len(self.hand) >= 2:
            return False
        return True


@pytest.fixture
def one_twist_player() -> OneTwistPlayer:
    return OneTwistPlayer()
