from lang.letter import Letter

"""
capitalize_all : [Letter] -> [Letter]
    {l:Letter} -> A
"""


def capitalize(inputs: list[str]) -> list[str]:
    return list([s.capitalize() for s in inputs])
