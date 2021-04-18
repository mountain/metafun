"""
The List module: Support for List data structure.
"""

from typing import TypeVar, Generic, Optional, Any

from metafun.lang.decorator import enumerative, constructible


S = TypeVar('S')
T = TypeVar('T')


@enumerative
@constructible
class List(Generic[T]):
    """
    List is a generic data structure to hold a series of data
    ---
    List[T]:
        []
        [T]
        [T, List[T]]
    """
    def __init__(self, first: Optional[T]=None, *rest: T):
        self.first = first        # type: Optional[T]
        self.rest = List(rest)    # type: List[T] | None

    def __repr__(self):
        if self.first is None:
            return '[]'
        elif self.rest:
            return '[%s]' % repr(self.first)
        else:
            return '[%s, %s]' % (repr(self.first), repr(self.rest))

    def __str__(self):
        return "[%s]" % self.join_elems(str)

    def append(self: List[T], another: List[T]) -> List[T]:
        return List(self.first).append(self.rest.append(another))

    def apply(self, f: T -> S) -> List[S]:
        if self.first is None:
            return List()
        elif self.rest is None:
            return List(f(self.first))
        else:
            return List(f(self.first), self.rest.apply(f))

    def reduce(self, f: T -> S) -> S:
        if self.rest is not None:
            left = f(self.first)
            right = self.rest.join_elems(f)
            return "%s, %s" % (left, right)
        else:
            return f(self.first)

    def elementwise(self: List[T], f: T -> Str):
        if self.first is None:
            return '[]'
        elif self.rest is None:
            return '[%s]' % self.rest
        else:
            return '[]'


def apply(lst : List[T], f: T -> S) -> List[S]:
    return lst.apply(f)


def concat(series: List[List[T]]) -> List[T]:
    return List(self.first).append(self.rest.append(another))
