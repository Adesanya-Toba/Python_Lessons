"""
A decorator is a callable that takes another function as an argument (the decorated
function).
A decorator may perform some processing with the decorated function, and returns
it or replaces it with another function or callable object.

In other words, assuming an existing decorator named decorate, this code:
@decorate
def target():
    print('running target()')

has the same effect as writing this:
def target():
    print('running target()')

target = decorate(target)

The end result is the same: at the end of either of these snippets, the target name is
bound to whatever function is returned by decorate(target)—which may be the
function initially named target, or may be a different function.
"""

import time


# Example 9.1
def deco(func):
    def inner():
        print("running inner()")

    return inner


# Decorators are executed immediately the module is loaded, i.e.,
# right after the decorated function is defined, which is usually at import time.
@deco  # Adding the decorator here replaces the function with a different one.
def target():
    print("running target()")


target()  # This actually runs inner()

print(target)  # target is now a reference to inner.

# Example 9.2
print("\n", "#" * 40, "\n")
registry = []


def register(func):
    print(f"running register({func})")  # Runs at Import time
    registry.append(func)
    return func  # We must return a function


@register
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


def f3():
    print("running f2()")


def main():
    print("running main()")
    print("registry ->", registry)
    f1()  # Runs at runtime
    f2()
    f3()


# Example 9.14
print("\n", "#" * 40, "\n")


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
        print(f"[{elapsed:0.8f}]  {name}({arg_str}) -> {result!r}")
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


# snooze = clock(snooze) # Replacing snooze with the output function from clock
# snooze(0.123)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


print("*" * 40, "Calling snooze(.123)")
snooze(0.123)
print("*" * 40, "Calling factorial(6)")
print("6! =", factorial(6))
