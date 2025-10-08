from enum import Enum


class Route(str, Enum):
    INDEX = "/"
    ADVISOR = "/advisor"
    INVESTMENTS = "/investments"
    REAL_ESTATE = "/real-estate"
