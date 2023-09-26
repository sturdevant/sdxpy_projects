from hashlib import sha256

example = bytes("hash", "utf-8")
for i in range(1, len(example) + 1):
    substring = example[:i]
    hash = sha256(substring).hexdigest()
    print(f"{substring}\n{hash}")
