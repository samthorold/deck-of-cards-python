from card_games.deck import DeckInterface
from card_games.games.blackjack import PlayerInterface, Game


def test_game_player_bust(
    always_twist_player: PlayerInterface, tens_deck: DeckInterface
) -> None:
    players = [always_twist_player]
    game = Game(players, tens_deck)
    game.game_turn()
    assert game.is_bust(game.players[0])


def test_game_house_bust(
    never_twist_player: PlayerInterface, fifteen_then_ten_deck: DeckInterface
) -> None:
    players = [never_twist_player]
    game = Game(players, fifteen_then_ten_deck)
    game.game_turn()
    assert game.is_bust(game.house)


def test_game_house_wins(
    one_twist_player: PlayerInterface, tens_deck: DeckInterface
) -> None:
    players = [one_twist_player]
    game = Game(players, tens_deck)
    game.game_turn()
    assert not game.is_bust(game.house)
    assert not game.is_bust(game.players[0])


def test_game_player_wins(
    one_twist_player: PlayerInterface, tens_then_nines_deck: DeckInterface
) -> None:
    players = [one_twist_player]
    game = Game(players, tens_then_nines_deck)
    game.game_turn()
    assert not game.is_bust(game.house)
    assert not game.is_bust(game.players[0])
