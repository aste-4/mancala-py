class Pit:
    """
    Class representing one pit on the board in Mancala.
    """

    NORMAL_PIT_SYMBOL = '[]'
    GOAL_PIT_SYMBOL = '<>'

    def __init__(self, stone_count: int, is_goal: bool = False):
        """
        Constructor method.

        Args:
            stone_count (int): The number of stones in this pit.
            is_goal (bool, optional): True if this is a goal pit. Defaults to False.
                                      If True, this pit is treated as a goal pit.

        Raises:
            ValueError: If stone_count is negative.
        """
        if stone_count < 0:
            raise ValueError('stone_count must be non-negative')
        self.stone_count = stone_count
        self.is_goal = is_goal

    def add_stone(self) -> None:
        """
        Add a stone to this pit.
        """
        self.stone_count += 1

    def take_all_stones(self) -> int:
        """
        Removes all stones from this pit and returns the number of removed stones.
        After this operation, the pit becomes empty.

        Returns:
            int: The number of stones taken from this pit.
        """
        stones = self.stone_count
        self.stone_count = 0
        return stones

    def __repr__(self):
        """
        Returns a string representation of this pit for debugging purposes.

        Returns:
            str: A string representation of this pit.
        """
        return f'Pit(stone_count={self.stone_count}, is_goal={self.is_goal})'

    def __str__(self):
        """
        Returns a string representation of this pit.

        Returns:
            str: A string representation of this pit.
            example: [04] (normal pit) or <00> (goal pit)
        """
        if self.is_goal:
            return f'{self.GOAL_PIT_SYMBOL[0]}{self.stone_count:02}{self.GOAL_PIT_SYMBOL[1]}'
        else:
            return f'{self.NORMAL_PIT_SYMBOL[0]}{self.stone_count:02}{self.NORMAL_PIT_SYMBOL[1]}'
