# Testing my knowledge of decorators


def retry(func):
    def retried_func(*args):
        MAX_TRIES = 3
        tries = 0

        print("In retried function", *args)

        while tries < MAX_TRIES:
            try:
                result = func(*args)
                return result
            except Exception:
                tries += 1

    return retried_func


@retry
def test_hello(val: int):
    print("This is a test!", val)
    # raise Exception
    return val * 100


print(test_hello(35))
