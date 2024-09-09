import os

print("Hello..")
print(os.name)

return_string = "toba23?rir"

if return_string.find("?") != -1:
    return_string += "&"
    print(return_string.find("@"))
    print("here")

separator = "/"
key = ""
key_list = key.split(separator)
key_list.pop()
print(key_list)

combined_str = separator.join(key_list) + separator
print(combined_str)

before, sep, after = key.partition("/")

print(before, sep, after)
new_key = key.removesuffix("")
print(new_key)

# Creating a new type in python
from typing import Union
from typing_extensions import TypeAlias

special_var: TypeAlias = Union[str, int, None]
# special_var2: TypeAlias = str | int | None # requires python 3.10

_sp_str: special_var = "hello"
print(_sp_str.upper())
