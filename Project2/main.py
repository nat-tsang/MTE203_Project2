#!/usr/bin/env python3

import base64

def main():
    print("wassup natalie")
    print("https://www.youtube.com/watch?v=sOTBU5QJJWM")

    s = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    
    print(hex_to_base64(s))

def hex_to_base64(s):
    return base64.b64encode(base64.b16decode(s.upper())).decode()

if __name__ == "__main__":
    main()

