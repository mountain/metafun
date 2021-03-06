from lang.letter import Letter

"""
capitalize : Letter -> Letter
    a -> A
    b -> B
    c -> C
    d -> D
    e -> E
    f -> F
    g -> G
    h -> H
    i -> I
    j -> J
    k -> K
    l -> L
    m -> M
    n -> N
    o -> O
    p -> P
    q -> Q
    r -> R
    s -> S
    t -> T
    u -> U
    v -> V
    w -> W
    x -> X
    y -> Y
    z -> Z
"""


def capitalize(inputs: list[str]) -> list[str]:
    return list([s.capitalize() for s in inputs])
