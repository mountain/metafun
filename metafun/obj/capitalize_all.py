from lang.letter import Letter

"""
capitalize_all : List[Letter] -> List[Letter]
    x -> capitalize a
    x, xs -> capitalize a, capitalize_all xs
"""


def capitalize(inputs: list[str]) -> list[str]:
    return list([s.capitalize() for s in inputs])
