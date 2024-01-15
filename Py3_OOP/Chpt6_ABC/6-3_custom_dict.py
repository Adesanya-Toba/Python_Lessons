# We're going to create a dictionary-like mapping from some key
# to – well – an object of any possible type
#
# BaseMapping = abc.Mapping[Comparable, Any]
#
# We've defined the key with the type Comparable because we
# want to be able to compare the keys and sort them into order

from __future__ import annotations
from collections import abc
from typing import Protocol, Any, overload, Union
import bisect
from typing import Iterator, Sequence, Iterable


class Comparable(Protocol):
    def __eq__(self, other: object) -> bool:
        ...

    def __ne__(self, other: object) -> bool:
        ...

    def __le__(self, other: object) -> bool:
        ...

    def __lt__(self, other: object) -> bool:
        ...

    def __ge__(self, other: object) -> bool:
        ...

    def __gt__(self, other: object) -> bool:
        ...


BaseMapping = abc.Mapping[Comparable, Any]


class Lookup(BaseMapping):
    @overload
    def __init__(self, source: Iterable[tuple[Comparable, Any]]) -> None:
        ...

    @overload
    def __init__(self, source: BaseMapping) -> None:
        ...

    def __init__(
        self, source: Union[Iterable[tuple[Comparable, Any]], BaseMapping, None] = None
    ) -> None:
        sorted_pairs: Sequence[tuple[Comparable, Any]]
        if isinstance(source, Sequence):
            sorted_pairs = sorted(source)
        elif isinstance(source, abc.Mapping):
            sorted_pairs = sorted(source.items())
        else:
            sorted_pairs = []

        self.key_list = [p[0] for p in sorted_pairs]
        self.value_list = [p[1] for p in sorted_pairs]

    def __len__(self) -> int:
        return len(self.key_list)

    def __iter__(self) -> Iterator[Comparable]:
        return iter(self.key_list)

    def __contains__(self, key: object) -> bool:
        index = bisect.bisect_left(self.key_list, key)
        return key == self.key_list[index]

    def __getitem__(self, key: Comparable) -> Any:
        index = bisect.bisect_left(self.key_list, key)
        if key == self.key_list[index]:
            return self.value_list[index]
        raise KeyError(key)


def main():
    x = Lookup([["z", "Zillah"], ["a", "Amy"], ["c", "Clara"], ["b", "Basil"]])
    print(x["c"])


if __name__ == "__main__":
    main()
