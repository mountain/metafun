from lang.object import Object
from lang.generative import generative


@generative
class Letter(Object):
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
        return "'%s'" % self.content

    def __str__(self):
        return self.content
