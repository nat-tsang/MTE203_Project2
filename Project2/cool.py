#!/usr/bin/env python3

from base64 import b16decode, b64encode
from operator import itemgetter
from typing import List, Tuple


def main():
    chain_lens: List[Tuple[int, int]] = [
        collatz_chain_len(i) for i in range(1, 1000000)
    ]
    print(max(chain_lens, key=itemgetter(1)))


def hex_to_base64(s: str) -> bytes:
    return b64encode(b16decode(s.upper()))


def collatz(n: int) -> int:
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def collatz_chain_len(n: int, debug: bool = False) -> Tuple[int, int]:
    original_n = n

    # init at one to include the 1 term
    count = 1
    while n != 1:
        if debug:
            print(n, end="->")
        n = collatz(n)
        count += 1
    if debug:
        print(n)
    return (original_n, count)


if __name__ == "__main__":
    main()
