import itertools
import typing


dox = {}
ctx = {
    '[]': [[]],
    '{}': [{}]
}


def qname(clazz: typing.Type):
    return '.'.join([clazz.__module__, clazz.__name__])


def readlines(lines: str):
    return [ln.strip() for ln in lines.split('\n') if ln.strip()]


def is_tuple(rule: str):
    rule = rule.strip()
    return ',' in rule

def is_list(rule: str):
    rule = rule.strip()
    return rule[0] == '[' and rule[-1] == ']'


def is_entity(rule: str):
    rule = rule.strip()
    return rule[0] == '{' and rule[-1] == '}'


def is_concrete(rule: str):
    if not rule:
        return False

    rule = rule.strip()
    if is_tuple(rule):
        for sub in subrules(rule):
            if not is_concrete(sub):
                return False

    rule = rule.strip()
    if is_list(rule):
        return rule == '[]' or rule[1:-1] in ctx

    if is_entity(rule):
        return rule == '{}' or is_concrete(rule[1:-1])

    try:
        param = rule[rule.index('[') + 1:rule.rindex(']')]
        return False
    except ValueError as e:
        return '[' not in rule and ']' not in rule


def list_rule(depth: int, ctx: dict, rule: str):
    subs = subrules(rule[1:-1])
    vals = itertools.product([ctx[sub] if sub in ctx else sub for sub in subs])
    for lst in vals:
        for val in lst[0]:
            yield val


def subrules(rule: str):
    if rule[0] == '[' and rule[-1] == ']':
        rule = rule[1:-1]
    return [rl.strip() for rl in rule.split(',') if rl.strip()]


def eval_rule(depth: int, ctx: dict, rule: str):
    if depth < 4:
        if rule in ctx:
            return ctx[rule]
        else:
            import metafun
            ctx.update(locals())
            val = eval(rule, ctx)
            ctx[rule] = val
            return val


def gen_by_cases(depth, clazz: typing.Type, rules: typing.List[str]) -> typing.Generator:
    if depth < 4:
        for rule in rules:
            if is_concrete(rule):
                if rule in ctx:
                    yield from eval_rule(depth + 1, ctx, rule)
                else:
                    if is_list(rule):
                        for p in list_rule(depth + 1, ctx, rule):
                            yield clazz(p)
                    else:
                        yield clazz(rule)


def generate(clazz: typing.Type) -> typing.Generator:
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

