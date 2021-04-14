from typing import TypeVar, Generic
from lang.generative import generative


T = TypeVar('T')


@generative
class List(Generic[T]):
    """
        T
        T, lang.list.List[T]
    """
    def __init__(self, *instances):
        self.first = instances[0]
        self.rest = None if len(instances) < 2 else instances[1]
