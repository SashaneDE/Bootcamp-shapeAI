import hashlib

result = hashlib.md5(b"sashane")

print("The Byte equivalent for sashane is: ", end="")
print(result.digest())