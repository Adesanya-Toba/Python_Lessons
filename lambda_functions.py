rtn_x = lambda x: print(x + 1)
rtn_x(3)

full_name = lambda first, last: f"Full name: {first.title()} {last.title()}"
print(full_name("toba", "adesanya"))

# Immediately Invoked Function Expression
(lambda x, y: print(x + y))(2, 3)

# Lambda functions are frequently used with high-order functions, which
# take on or more functions as arguments or return one or more functions

high_ord_func = lambda x, func: print(x + func(x))
high_ord_func(2, lambda x: x * x)
