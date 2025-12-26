import math
from decorators_module import log_call

@log_call
def f_linear(x):
    return x

@log_call
def f_square(x):
    return x ** 2

@log_call
def f_cube(x):
    return x ** 3

@log_call
def f_sin(x):
    return math.sin(x)

@log_call
def f_cos(x):
    return math.cos(x)

FUNCTIONS = {
    "1": ("y = x", f_linear),
    "2": ("y = x^2", f_square),
    "3": ("y = x^3", f_cube),
    "4": ("y = sin(x)", f_sin),
    "5": ("y = cos(x)", f_cos),
}
