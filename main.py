import math
import os


def add(a, b) -> int:
    return math.floor(a + b)


def div(a, b) -> int:
    return int(a / b)


def pow(a, b) -> int:
    return int(a**b)



def to_sentence(s) -> str:
    s = s.capitalize()

    if s.endswith('.'):
        return s
    else:
        return s + '.'
