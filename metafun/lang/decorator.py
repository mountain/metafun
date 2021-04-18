import typing
import itertools


dox = {}
ctx = {}


def qname(clazz: typing.Type):
    return '.'.join([clazz.__module__, clazz.__name__])


def readlines(lines: str):
    return [ln.strip() for ln in lines.split('\n') if ln.strip()]


def subrules(rule: str):
    return [rl.strip() for rl in rule.split(',') if rl.strip()]


def gen_by_cases(depth, clazz: typing.Type, rules: typing.List[str]) -> typing.Generator:
    if depth < 4:
        for rule in rules:
            if rule:
                if rule in ctx:
                    yield from ctx[rule]
                else:
                    subs = subrules(rule)
                    vals = itertools.product([ctx[sub] if sub in ctx else sub for sub in subs])
                    clzs = [eval(sub, ctx) if sub in ctx else str for sub in subs]
                    for val, cls in zip(vals, clzs):
                        p = cls(val[0])
                        yield  clazz(p)


def enumerative(clazz: typing.Type) -> typing.Type:
    return clazz


def constructible(clazz: typing.Type) -> typing.Type:
    qn = qname(clazz)
    rules = clazz.__doc__
    dox[qn] = rules
    ctx[qn] = list(gen_by_cases(0, clazz, readlines(rules)))
    return clazz


def generate(clazz: typing.Type) -> typing.Generator:
    ctx.update(locals())

    g = []
    match type(clazz):
        case t if issubclass(t, type):
            qn = qname(clazz)
            g = ctx[qn]
        case other if issubclass(other, typing._GenericAlias):
            qn = repr(clazz)
            bn = qn[:qn.index('[')]
            rules = dox[bn]
            for param in clazz.__args__:
                pn = qname(param)
                rules = rules.replace('T', pn)

            g = gen_by_cases(0, clazz, readlines(rules))
            ctx[qn] = g

    yield from g

