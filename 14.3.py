def convert(num, to_base=10, from_base=10):
    n = int(num, from_base) if isinstance(num, str) else num
    alp = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
    res = ''
    while n > 0:
        n, m = divmod(n, to_base)
        res += alp[m]
    return res[::-1]


s = (16**302)-(4**578)-(2**141)+24
s1 = convert(s, to_base=2, from_base=10)
print(s1.count('0'))
