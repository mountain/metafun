from metafun.lang.decorator import constructible


@constructible
class Entity:
    """
        {}
    """
    def __init__(self, **bindings):
        self.content = dict(**bindings)
