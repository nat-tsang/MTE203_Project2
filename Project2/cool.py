#!/usr/bin/env python3

from base64 import b16decode, b64encode
from typing import List, Tuple


def main() -> None:
    bad_blood = """
    'Cause baby now we got bad blood
    You know it used to be mad love
    So take a look at what you've done
    'Cause baby now we got bad blood

    Now we got problems
    And I don't think we can solve them
    You made a really deep cut
    And baby now we got bad blood

    Did you have to do this?
    I was thinking that you could be trusted
    Did you have to ruin what was shining now it's all rusted
    Did you have to hit me where I'm weak baby I couldn't breathe
    I rubbed it in so deep
    Salt in the wound like you're laughing right at me
    Oh, it's so sad to think about the good times
    You and I

    'Cause baby now we got bad blood
    You know it used to be mad love
    So take a look at what you've done
    'Cause baby now we got bad blood

    Now we got problems
    And I don't think we can solve them
    You made a really deep cut
    And baby now we got bad blood

    Did you think we'd be fine?
    Still got scars on my back from your knife
    So don't think it's in the past
    These kind of wounds they last and they last
    Now did you think it all through?
    All these things will catch up to you
    And time can heal but this won't
    So if you come in my way, just don't
    Oh, it's so sad to think about the good times
    You and I

    'Cause baby now we got bad blood
    You know it used to be mad love
    So take a look at what you've done
    'Cause baby now we got bad blood

    Now we got problems
    And I don't think we can solve them
    You made a really deep cut
    And baby now we got bad blood

    Band-aids don't fix bullet holes
    You say sorry just for show
    You live like that, you live with ghosts (Ghosts)
    Band-aids don't fix bullet holes (Hey!)
    You say sorry just for show (Hey!)
    You live like that, you live with ghosts (Hey!)
    Hm, if you love like that blood runs cold

    'Cause baby now we got bad blood
    You know it used to be mad love
    So take a look at what you've done
    'Cause baby now we got bad blood

    Now we got problems
    And I don't think we can solve them (Think we can solve them)
    You made a really deep cut
    And baby now we got bad blood

    'Cause baby now we got bad blood
    You know it used to be mad love
    So take a look at what you've done (Look at what you've done)

    'Cause baby now we got bad blood (Woah)
    Now we got problems
    And I don't think we can solve them
    You made a really deep cut
    And baby now we got bad blood (Hey!)
    """
    print(bad_blood)


def hex_to_base64(s: str) -> bytes:
    return b64encode(b16decode(s.upper()))


def collatz(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def numstr_to_ints(s: str) -> List[int]:
    return [int(c) for c in s]


def sliding_window_of_string(s: str, window_size: int) -> List[str]:
    return [s[i : i + window_size] for i in range(len(s) - window_size + 1)]


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
