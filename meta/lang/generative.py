import typing
import itertools


dox = {}
ctx = {}

def qname(clazz: typing.Type):
    return '.'.join([clazz.__module__, clazz.__name__])


def readlines(lines: str):
    return [ln.strip() for ln in lines.split('\n') if ln.strip()]


def gen_by_cases(clazz: typing.Type, cases: typing.List[str]) -> typing.Generator:
    loc = {}
    match definition.split(','):
        case first, rest:

        case _:
            loc[definition] = "'%s'" % _
            instances = eval(definition, ctx, loc)
            yield clazz(instances)
    instances = [ctx[qname(inst)] if type(inst) == type else inst for inst in instances]



def generative(clazz: typing.Type) -> typing.Type:
    qn = qname(clazz)
    definitions = clazz.__doc__
    dox[qn] = definitions
    ctx[qn] = gen_by_cases(clazz, readlines(definitions))
    return clazz


def generate(clazz: typing.Type) -> typing.Generator:
    import lang
    import lang.object
    import lang.list
    import lang.letter

    ctx.update(locals())

    g = []
    match type(clazz):
        case t if issubclass(t, type):
            qn = qname(clazz)
            g = ctx[qn]
        case other if issubclass(other, typing._GenericAlias):
            qn = repr(clazz)
            bn = qn[:qn.index('[')]
            definitions = dox[bn]
            for param in clazz.__args__:
                pn = qname(param)
                definitions = definitions.replace('T', pn)

            g = gen_by_cases(clazz, readlines(definitions))
            ctx[qn] = g

    yield from g

