from metafun.lang.entity import Entity
from metafun.lang.decorator import enumerative, constructible


@enumerative
@constructible
class Digit(Entity):
    """
    Digit: {content: }
        0
        1
        2
        3
        4
        5
        6
        7
        8
        9
    """
    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '%s' % self.content

    def __str__(self):
        return self.content

    def __eq__(self, another):
        return isinstance(another, type(self)) and self.content == another.content

    def __gt__(self, another):
        return self.content > another.content

    def __lt__(self, another):
        return self.content < another.content
