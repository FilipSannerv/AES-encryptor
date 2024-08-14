#Example key and block to encrypt in hex
key_hex = "F4C020A0A1F604FD343FAC6A7E6AE0F9"
block_hex = "F295B9318B994434D93D98A4E449AFD8"

key_bytes = bytes.fromhex(key_hex)
block_bytes = bytes.fromhex(block_hex)

with open("input.bin", "wb") as f:
    f.write(key_bytes)
    f.write(block_bytes)

print("File created successfully")

