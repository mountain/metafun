import typing

from metafun.lang import dox, ctx, qname, readlines, gen_by_cases


def enumerative(clazz: typing.Type) -> typing.Type:
    return clazz


def constructible(clazz: typing.Type) -> typing.Type:
    qn = qname(clazz)
    rules = clazz.__doc__
    dox[qn] = rules
    ctx[qn] = list(gen_by_cases(0, clazz, readlines(rules)))
    return clazz

