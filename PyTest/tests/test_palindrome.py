# Running pytest with the parameterization mark
# This allows pytest to create different variants of our test using a single
# test definition,
# based on parameters we specify.

import pytest


# function which return reverse of a string
def is_palindrome(s):
    return s == s[::-1]


# The first argument in the mark is the parameter name. It can be more than one
# The second argument is a list of either tuples or single values that
# represents the parameter value(s).


@pytest.mark.parametrize(
    "palindrome",
    [
        "",
        "a",
        pytest.param("Bob", marks=pytest.mark.skip),
        pytest.param("Never odd or even", marks=pytest.mark.skip),
        pytest.param("Do Geese see God?", marks=pytest.mark.skip),
    ],
)
def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)


@pytest.mark.parametrize(
    "non_palindrome",
    [
        "abc",
        "abab",
    ],
)
def test_is_palindrome_not_palindrome(non_palindrome):
    assert not is_palindrome(non_palindrome)
