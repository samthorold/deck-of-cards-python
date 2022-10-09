"""
N players.

House is a player, but with rules governing actions.

A player's turn may involve 1+ draws and they are either free to "stick" or
"twist" or are "bust" after each draw.


"""


from dataclasses import dataclass


@dataclass
class Player:
    name: str
