print(dir(int))
num = 7
print(num.to_bytes(3, 'big'))
print(int.from_bytes(b'\x00\x00\x07', 'big'))