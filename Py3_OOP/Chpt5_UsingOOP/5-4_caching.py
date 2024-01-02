import time

from urllib.request import urlopen
from typing import Optional, List


class Webpage:
    def __init__(self, url: str):
        self.url = url
        self._content: Optional[bytes] = None

    @property
    def content(self) -> bytes:
        if self._content is None:
            print("Retrieving New page...")
            with urlopen(self.url) as response:
                self._content = response.read()
        return self._content


class AverageList(List[int]):
    @property
    def average(self) -> float:
        return sum(self) / len(self)


def main():
    webpage = Webpage("https://ccphillips.net/")

    now = time.perf_counter()
    content1 = webpage.content
    first_fetch = time.perf_counter() - now

    now = time.perf_counter()
    content2 = webpage.content
    second_fetch = time.perf_counter() - now

    assert content2 == content1, "Problem: Pages were different"
    print(f"Initial Request {first_fetch:.8f}")
    print(f"Subsequent Requests {second_fetch:.8f}")

    a = AverageList([10, 15, 12, 45, 68, 9, 20, 48, 19])
    print(a.average)


if __name__ == "__main__":
    main()
