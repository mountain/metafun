from metafun.lang.entity import Entity
from metafun.lang.decorator import constructible


@constructible
class Letter(Entity):
    """
        a
        b
        c
        d
        e
        f
        g
        h
        i
        j
        k
        l
        m
        n
        o
        p
        q
        r
        s
        t
        u
        v
        w
        x
        y
        z
        A
        B
        C
        D
        E
        F
        G
        H
        I
        J
        K
        L
        M
        N
        O
        P
        Q
        R
        S
        T
        U
        V
        W
        X
        Y
        Z
    """
    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '%s' % self.content

    def __str__(self):
        return self.content

    def __eq__(self, another):
        return self.content == another.content

    def __gt__(self, another):
        return self.content > another.content

    def __lt__(self, another):
        return self.content < another.content
