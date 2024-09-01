# Simple XOR Byte Stream Decryptor
import sys
ARGS = sys.argv

USAGE = f"""
Simple XOR Byte Strem Decryptor

    Decrypts a file that uses a simple byte-stream XOR cipher

Usage:

    python3 {ARGS[0]} encrypted_file decrypted_file [xor_key_in_hex]

        xor_key_in_hex: XOR key as a hexadecimal string (OPTIONAL)

    For example:
        python3 {ARGS[0]} deathstar_blueprint.enc rebel_plan.exe 9a

"""

XORKEY = '5e'

if len(ARGS) == 1:
    print(USAGE)
    sys.exit(0)
elif len(ARGS) == 4:
    XORKEY = ARGS[3]
elif len(ARGS) != 3:
    print(USAGE)
    sys.exit(1)

key = int(XORKEY, 16)

with open(str(ARGS[1]), "rb") as src_file:
    with open(str(ARGS[2]), "ab") as dst_file:
        while(sb := src_file.read(1)):
            db = int.from_bytes(sb) ^ key
            dst_file.write(db.to_bytes(1))
