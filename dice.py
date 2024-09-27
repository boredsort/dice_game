import random
import logging

logger = logging.getLogger("dicegame")
class Dice:

    @staticmethod
    def roll()-> int:
        result = random.randint(1, 6) 
        logger.info(f'Rolled the dice result: {result}')
        return result