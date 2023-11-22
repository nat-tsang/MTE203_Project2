from cool import *  # noqa: F403
from operator import itemgetter, mul
from functools import reduce


def test_collatz_4():
    assert collatz(4) == 2


def test_collatz_chain_13():
    assert collatz_chain_len(13)[1] == 10


def test_hex_to_base64():
    s = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    assert (
        hex_to_base64(s)
        == b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    )


def test_collatz_chain_837799():
    """
    Oh, it's so sad to think about the good times
    You and I
    'Cause baby, now we got bad blood
    You know it used to be mad love
    So take a look what you've done
    'Cause baby, now we got bad blood, hey!
    """
    assert collatz_chain_len(837799)[1] == 525


def test_i_got_two_glock_40s_them_be_20_twins():
    """
    I can't take it back, look where I'm at (Uh)
    We was OG like D.O.C., remember that? (Remember that?)
    My TLC was quite OD, ID my facts (ID my)
    Now POV of you and me, similar Iraq
    I don't hate you, but I hate to critique, overrate you
    These beats of a dark heart, use basslines to replace you
    Take time and erase you, love don't hear no more
    No, I don't fear no more
    Better yet, respect ain't quite sincere no more, ah!
    """

    baghead_milonakis = (
        """73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450""".strip()
        .replace("\n", "")
        .replace(" ", "")
    )

    desert_storm = sliding_window_of_string(baghead_milonakis, 13)
    products = [
        (reduce(mul, numstr_to_ints(s)), numstr_to_ints(s)) for s in desert_storm
    ]
    prod, sequence = max(products, key=itemgetter(0))
    assert prod == 23514624000
    assert sequence == [5, 5, 7, 6, 6, 8, 9, 6, 6, 4, 8, 9, 5]
