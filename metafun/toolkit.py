from arghandler import *

from metafun.tool.sampler import main as smpmain
from metafun.tool.interpreter import main as itpmain


@subcmd
def help(parser, context, args):
    pass


@subcmd('sample', help='sample a collection of random programs by a generative meta-program')
def sample(parser, context, args):
    parser.add_argument("-n", "--num", type=int, default='1',
        help="number of programs to generate")
    parser.add_argument("-o", "--output", type=int, default='1',
        help="number of programs to generate")
    parser.add_argument("-m", "--module", type=str, default='',
        help="module to a generative meta-program")
    opt = parser.parse_args(args)

    smpmain(context, opt)


@subcmd('interp', help='interpret a program')
def interp(parser, context, args):
    parser.add_argument("-m", "--module", type=str, default='',
        help="module to a program")
    opt = parser.parse_args(args)

    itpmain(context, opt)


def main():
    import sys

    handler = ArgumentHandler()
    if len(sys.argv) < 2:
        handler.run(['help'])
    else:
        handler.run(sys.argv[1:])
