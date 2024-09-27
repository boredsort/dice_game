import logging
import os
from typing import List
from time import time

from dice import Dice


class Game:
    # Task 1.1 Create a Game
    def __init__(self, logger):
        self._logger = logger


    def one_or_six(self, first:int, second:int)-> bool:
        # Task 1.5 Use proper documents with doctstring
        """validate the if the values are either 1 or 6

        Args:
            first (int): values 1 - 6 range for the first dice roll
            second (int): values 1 - 6 range for the second dice roll

        Returns:
            bool: True if 1 or 6 
        """
        valid_result: List[int] = [1, 6]
        return all([
            first in valid_result,
            second in valid_result
        ])
    

    def double_six(self, first:int, second:int)-> bool:
        """validate the if the first and second dice roll are all 6

        Args:
            first (int): values 1 - 6 range for the first dice roll
            second (int): values 1 - 6 range for the second dice roll

        Returns:
            bool: True if booth are 6
        """
        return first == 6 and second == 6
    
    
    def double_one(self, first:int, second:int)-> bool:
        """validate the if the first and second dice roll are all 1

        Args:
            first (int): values 1 - 6 range for the first dice roll
            second (int): values 1 - 6 range for the second dice roll

        Returns:
            bool: True if booth are 1
        """
        return first == 1 and second == 1
        

    def start(self)-> List:
        """Dice Game that makes player win draw if player gets double 6 
        and allows a retry, if player gets double 1 then only gets a retry, 
        other numbers returns the result immediately and ends the game.

        Returns:
            List: Returns a List or an empty list
        """
        # Rule D
        draw = 3
        result = []
        for n in range(0, draw):
            self._logger.info(f"Draw no. {n+1}")
            first = Dice.roll()
            second = Dice.roll()
            # Rule A.
            # negate the one_or_six to check for numbers 
            # other than 1 or 6
            if not self.one_or_six(first, second):
                self._logger.info("Unlucky")
                result.append((first, second))
                break
            # Rule B
            if self.double_six(first, second):
                self._logger.info("Valid result")
                result.append((first, second))
                self._logger.info("Next Draw")
                continue
            # Rule C
            if self.double_one(first, second):
                self._logger.info("Skipping")
                self._logger.info("Next Draw")
                continue

        return result
    

if __name__ == '__main__':

    logger = logging.getLogger('dicegame')
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    timestamp = int(time())
    directory = 'logs'
    os.makedirs(directory, exist_ok=True)
    # Task 1.4 Log results to file
    file_handler = logging.FileHandler(f'logs/log_file_{timestamp}.log')
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    exit = False
    while not exit:
        # Task 1.3 CLI to specify the number of simulations
        tries = input("how many tries do you want?\n")
        simulations = int(tries)
        for n in range(0, simulations):
            logger.info(f"============== Game no: {n+1} ================")
            result = Game(logger).start()

        try_again = input("Try again? [Y/y] Yes, [Any] - Exit\n")
        if try_again.lower() != 'y':
            exit = True