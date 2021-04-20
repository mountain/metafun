"""
The List module: Support for List data structure.
"""

from typing import TypeVar, Generic, Optional, Callable

from metafun.lang.decorator import enumerative, constructible


S = TypeVar('S')
T = TypeVar('T')


@enumerative
@constructible
class List(Generic[T]):
    """
        {"first": None, "rest": None}
        {"first": T, "rest": None}
        {"first": T, "rest": metafun.lang.list.List[T]}
    """
    def __init__(self, first: Optional[T] = None, rest: 'metafun.lang.list.List[T]' = None):
        self.first = first  # type: Optional[T]
        self.rest = rest    # type: metafun.lang.list.List[T]

    def __repr__(self):
        if self.first is None:
            return '[]'
        elif self.rest is None:
            return '[%s]' % repr(self.first)
        else:
            return '[%s, %s]' % (repr(self.first), repr(self.rest))

    def __str__(self):
        def accum(elem: str, accumulated: str) -> str:
            return '%s, %s' % (elem, accumulated)

        return '[%s]' % self.apply(str).reduce(accum, '')[:-2]

    def append(self: List[T], another: List[T]) -> List[T]:
        return List(self.first).append(self.rest.append(another))

    def apply(self, f: Callable[T, S]) -> List[S]:
        if self.first is None:
            return List[S]()
        elif self.rest is None:
            return List[S](first=f(self.first))
        else:
            return List[S](first=f(self.first), rest=self.rest.apply(f))

    def reduce(self, f: Callable[[T, S], S], init: S) -> S:
        if self.first is None:
            return init
        elif self.rest is None:
            return f(self.first, init)
        else:
            return f(self.first, self.rest.reduce(f, init))


def apply(lst: List[T], f: Callable[T, S]) -> List[S]:
    return lst.apply(f)


def concat(series: List[List[T]]) -> List[T]:
    return List(self.first).append(self.rest.append(another))
