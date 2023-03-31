#!/usr/bin/python3

#
# XOR strings (ascii strings and hex strings).
#

MSG   = "A message"
HEX_1 = "aabbccddeeff1122334455"
HEX_2 = "1122334455778800aabbdd"

# XOR two bytearrays
def xor(first, second):
   return bytearray(x^y for x,y in zip(first, second))

D1 = bytes(MSG, 'utf-8')      # Convert ascii string to bytearray
D2 = bytearray.fromhex(HEX_1) # Convert hex string to bytearray
D3 = bytearray.fromhex(HEX_2) # Convert hex string to bytearray

r1 = xor(D1, D2)
r2 = xor(D2, D3)
r3 = xor(D2, D2)
print(r1.hex())
print(r2.hex())
print(r3.hex())
