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
        match instances:
            case first, rest:
                self.first = first
                self.rest = rest
            case first:
                self.first = first
                self.rest = None

    def join_elems(self, f):
        if self.rest is not None:
            left = f(self.first)
            right = self.rest.join_elems(f)
            return "%s, %s" % (left, right)
        else:
            return f(self.first)

    def __repr__(self):
        return "[%s]" % self.join_elems(repr)

    def __str__(self):
        return "[%s]" % self.join_elems(str)
