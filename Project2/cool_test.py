from cool import collatz, collatz_chain_len, hex_to_base64


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
