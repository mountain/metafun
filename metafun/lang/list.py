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
        []
        [T]
        [T, List[T]]
    """
    def __init__(self, first: Optional[T] = None, rest: 'List[T]' = None):
        self.first = first  # type: Optional[T]
        self.rest = rest    # type: List[T]

    def __repr__(self):
        if self.first is None:
            return '[]'
        elif self.rest is None:
            return '[%s]' % repr(self.first)
        else:
            return '[%s, %s]' % (repr(self.first), repr(self.rest))

    def __str__(self):
        if self.first is not None:
            first_str = str(self.first)
            if self.rest is None:
                elem_str = '%s ' % first_str
            else:
                elem_str = '%s, %s' % (first_str, str(self.rest)[1:-1])
        return '[%s]' % elem_str

    def append(self: List[T], another: List[T]) -> List[T]:
        return List(self.first).append(self.rest.append(another))

    def apply(self, f: Callable[T, S]) -> List[S]:
        if self.first is None:
            return List()
        elif self.rest is None:
            return List(f(self.first))
        else:
            return List(f(self.first), self.rest.apply(f))

    def reduce(self, f: Callable[T, S]) -> S:
        if self.rest is not None:
            left = f(self.first)
            right = self.rest.join_elems(f)
            return "%s, %s" % (left, right)
        else:
            return f(self.first)

    def elementwise(self: List[T], f: Callable[T, str]):
        if self.first is None:
            return '[]'
        elif self.rest is None:
            return '[%s]' % self.rest
        else:
            return '[]'


def apply(lst: List[T], f: Callable[T, S]) -> List[S]:
    return lst.apply(f)


def concat(series: List[List[T]]) -> List[T]:
    return List(self.first).append(self.rest.append(another))
