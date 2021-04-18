
class MFRProgram:
    """
    a map-filter-reduce style program
    ---
    MFRProgram:
        []
        [T]
        [T, List[T]]
    """
    def __init__(self, input, mapper, filterer, reducer):
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
