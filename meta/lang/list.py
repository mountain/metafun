from typing import TypeVar, Generic
from lang.generative import generative


T = TypeVar('T')


@generative
class List(Generic[T]):
    """
        T
        T, lang.list.List[T]
    """
    def __init__(self, instances):
        match instances:
            case first, rest:
                self.first = first
                self.rest = rest
            case first:
                self.first = first
                self.rest = []
