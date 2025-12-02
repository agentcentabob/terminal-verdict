"""Terminal.Exit package entrypoint."""
from .game_engine import GameEngine


def run():
    engine = GameEngine()
    engine.run()
