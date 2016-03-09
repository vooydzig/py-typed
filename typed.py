from functools import wraps

__all__ = ['accepts', 'returns']


def _validate_types(value, t):
    if not isinstance(value, t) or not issubclass(type(value), t):
        raise TypeError


def _validate_args_count(expected_arg_count, actual_arg_count):
    if not expected_arg_count == actual_arg_count:
        raise ValueError("Invalid type argument count")


def _validate_args_type(types, declared_args, actual_args):
    for arg, value in zip(declared_args, actual_args):
        _validate_types(value, types[arg])


def _validate_kwargs_type(types, kwargs):
    for k, v in kwargs.iteritems():
        _validate_types(v, types[k])


def accepts(**kwargs):
    def inner(f):
        @wraps(f)
        def wrapped(*args, **kwrds):
            code = f.__code__
            _validate_args_count(code.co_argcount, len(kwargs.keys()))
            _validate_args_type(kwargs, code.co_varnames, args)
            _validate_kwargs_type(kwargs, kwrds)
            return f(*args, **kwrds)

        return wrapped

    return inner


def returns(return_type):
    def inner(f):
        @wraps(f)
        def wrapped(*args, **kwrds):
            value = f(*args, **kwrds)
            _validate_types(value, return_type)
            return value

        return wrapped

    return inner


if __name__ == '__main__':

    @returns(int)
    @accepts(a=int, b=int)
    def add(a, b):
        return a + b


    add(1, 2)

    try:
        add(1.0, 2)
    except TypeError:
        print("Float is not an integer")
    try:
        add('1', 2)
    except TypeError:
        print("String is not an integer")
