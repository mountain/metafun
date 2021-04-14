ctx = {}


def mk_generator(clazz):
    loc = {}
    for ln in clazz.__doc__.split('\n'):
        defi = ln.lstrip()
        if defi:
            if defi not in ctx:
                loc[defi] = "'%s'" % defi
            instances = eval(defi, ctx, loc)
            yield clazz(instances)


def generative(clazz):
    qname = '.'.join([clazz.__module__, clazz.__name__])
    ctx[qname] = mk_generator(clazz)
    return clazz


def generate(clazz):
    qname = '.'.join([clazz.__module__, clazz.__name__])
    g = ctx[qname]
    yield from g

