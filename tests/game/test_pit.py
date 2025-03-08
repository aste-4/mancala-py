import pytest
from mancala_py.game.pit import Pit


class TestPit:
    def test_constructor_valid_stone_count(self):
        """Test that the constructor works with a valid stone count."""
        pit = Pit(5)
        assert pit.stone_count == 5
        assert pit.is_goal is False

        pit = Pit(0)
        assert pit.stone_count == 0
        assert pit.is_goal is False

        pit = Pit(10, is_goal=True)
        assert pit.stone_count == 10
        assert pit.is_goal is True

    def test_constructor_negative_stone_count(self):
        """Test that the constructor raises a ValueError if stone_count is negative."""
        with pytest.raises(ValueError):
            Pit(-1)

    def test_add_stone(self):
        """Test that add_stone() correctly increments the stone count."""
        pit = Pit(3)
        pit.add_stone()
        assert pit.stone_count == 4
        pit.add_stone()
        pit.add_stone()
        assert pit.stone_count == 6

    def test_take_all_stones(self):
        """Test that take_all_stones() correctly returns the number of stones and empties the pit."""
        pit = Pit(7)
        stones_taken = pit.take_all_stones()
        assert stones_taken == 7
        assert pit.stone_count == 0

        pit = Pit(0)
        stones_taken = pit.take_all_stones()
        assert stones_taken == 0
        assert pit.stone_count == 0

    def test_repr(self):
        """Test the __repr__ method."""
        pit = Pit(5)
        assert repr(pit) == "Pit(stone_count=5, is_goal=False)"

        pit = Pit(1, is_goal=True)
        assert repr(pit) == "Pit(stone_count=1, is_goal=True)"

    def test_str_normal_pit(self):
        """Test the __str__ method for a normal pit."""
        pit = Pit(4)
        assert str(pit) == "[04]"

        pit = Pit(0)
        assert str(pit) == "[00]"

        pit = Pit(10)
        assert str(pit) == "[10]"

    def test_str_goal_pit(self):
        """Test the __str__ method for a goal pit."""
        pit = Pit(0, is_goal=True)
        assert str(pit) == "<00>"

        pit = Pit(1, is_goal=True)
        assert str(pit) == "<01>"

        pit = Pit(15, is_goal=True)
        assert str(pit) == "<15>"
