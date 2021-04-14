from typing import TypeVar, Generic

from lang.letter import Letter

a = TypeVar('a')

"""
List a:
    a
    a, List a
"""


class List(Generic[a]):
    pass
