#!/usr/bin/env python3

CIPHERTEXT = b'\x17\x1d\n\n\x0b\x16\x13\t\x02\x08\x183\x10\x1f0\x1c\x02\x00\x02\x08\n*\x02\x00\x13\x1f\t\x1a*\x01\x00\x13\x14\x01\x16\n'


def decrypt(ciphertext: bytes, key: bytes) -> bytes:
    key_len = len(key)
    plain = []
    for i in range(len(ciphertext)):
        plain.append(ciphertext[i] ^ key[i % key_len])

    return bytes(plain)


def main():

    key = input('Please enter the password: ')
    key = key.encode()

    print('Your decrypted message is: ')
    plain = decrypt(CIPHERTEXT, key).decode('utf-8')
    print(plain)


if __name__ == '__main__':
    main()
