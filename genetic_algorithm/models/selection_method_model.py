from enum import Enum, auto

class SelectionMethod(Enum):
    TOURNAMENT = auto()
    ROULETTE = auto()
    ELITIST = auto()
    FITNESS = auto()
    RANDOM = auto()