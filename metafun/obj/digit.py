from metafun.lang.object import Object
from metafun.lang.decorator import enumerative, constructible


@enumerative
@constructible
class Digit(Object):
    """
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
        return '"%s"' % self.content

    def __str__(self):
        return self.content
