# tests/test_minesweeper.py

import pytest
import src.minesweeper as  minesweeper

def test_module_exists():
    assert minesweeper

def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    assert len(game.mines) == 2

def test_reveal():
    import random 
    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.reveal(0, 0)
    assert game.revealed == {(0, 0)}

def test_get_board():
    game = minesweeper.Minesweeper(3, 3, 2)
    assert game.get_board() == [[' ' for _ in range(3)] for _ in range(3)]

def test_is_winner():
    game = minesweeper.Minesweeper(3, 3, 2)
    assert game.is_winner() == False

def test_restart():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.restart()
    assert game.get_board() == [[' ' for _ in range(3)] for _ in range(3)]
    assert game.revealed == set()
    assert game.is_winner() == False      