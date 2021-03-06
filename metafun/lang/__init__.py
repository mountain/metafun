import itertools
import typing
import types
import copy


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
        check = not is_list(rule)
        for sub in subrules(rule):
            check = check or (sub in ctx)
        return check


    if is_list(rule):
        return rule == '[]' or rule[1:-1] in ctx

    if is_entity(rule):
        return rule == '{}' or is_concrete(rule[1:-1])

    try:
        param = rule[rule.index('[') + 1:rule.rindex(']')]
        return is_concrete('[%s]' % param)
    except ValueError as e:
        return '[' not in rule and ']' not in rule


def list_rule(depth: int, ctx: dict, rule: str):
    subs = subrules(rule[1:-1])
    evls = [eval_rule(depth + 1, ctx, sub) for sub in subs]
    vals = itertools.product(evls)
    for lst in vals:
        for val in lst[0]:
            yield val


def subrules(rule: str):
    if rule[0] == '[' and rule[-1] == ']':
        rule = rule[1:-1]
    return [rl.strip() for rl in rule.split(',') if rl.strip()]


def eval_rule(depth: int, ctx: dict, rule: str):
    import metafun
    ctx.update(locals())

    if depth < 4:
        if rule in ctx:
            tgt = ctx[rule]
            if isinstance(tgt, types.GeneratorType):
                lst = list(tgt)
                return lst
            else:
                cp = copy.copy(tgt)
                return cp

        evaluated = eval_rule(depth + 1, ctx, rule)
        return evaluated
    else:
        evaluated = eval(rule, ctx)
        if issubclass(type(evaluated), typing._GenericAlias):
            args = evaluated.__args__
            ctxparam = {
                qname(param): ctx[qname(param)] for param in args
            }
            d = typing.(evaluated)
            ctx[rule] = vals
            return vals



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
            nm = bn.split('.')[-1]
            rules = dox[bn]
            rules.replace(nm, bn)
            for param in clazz.__args__:
                pn = qname(param)
                rules = rules.replace('T', pn)

            g = gen_by_cases(0, clazz, readlines(rules))
            ctx[qn] = g

    yield from g

