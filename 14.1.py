def convert(num, to_base=10, from_base=10):
    n = int(num, from_base) if isinstance(num, str) else num
    alp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    while n > 0:
        n, m = divmod(n, to_base)
        res += alp[m]
    return res[::-1]


s = (16**385) - (4**726) - (2**298) + 3
s1 = convert(s, to_base=2, from_base=10)
print(s1.count('0'))