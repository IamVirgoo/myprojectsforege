def convert(num, to_base=10, from_base=10):
    n = int(num, from_base) if isinstance(num, str) else num
    alp = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
    res = ''
    while n > 0:
        n, m = divmod(n, to_base)
        res += alp[m]
    return res[::-1]


print(convert(int(input()), to_base=int(input()), from_base=int(input())))
