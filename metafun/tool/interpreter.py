import importlib


def main(context, opt):
    try:
        mdm = importlib.import_module(opt.module, package=None)
        if mdm is not None:
            pass
    except ImportError as e:
        print('failure when loading module')
        raise e
