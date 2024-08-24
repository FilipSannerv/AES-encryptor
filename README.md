# AES-128 algorithm implementation in C.

Reads key to use from stdin, followed by one or more blocks to encrypt using the key.

The 128-bit key is given as the first 16 bytes. Each block to encrypt consists of 16 bytes. Outputs the encrypted blocks as bytes.

Do not use this for encryption, instead use a standard library.

## Usage:

- Compile:

```
gcc aes-128.c -o aes-128
```

- <strong>hex_to_bytes.py</strong> creates an example binary input file with key written in hexadecimal:
F4C020A0A1F604FD343FAC6A7E6AE0F9 <br>
and encrypts one block: <br>
F295B9318B994434D93D98A4E449AFD8

- Expected encrypted block in hexadecimal is: <br>
52E418CBB1BE4949308B381691B109FE

- Run:

```
./aes-128 < input.bin
```

