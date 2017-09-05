import time as t


def pali(s):
    if s == s[::-1]:
        return True
    else:
        return False


before = t.time()
with open('foo.txt') as f:
    rv = {i.strip() for i in f if pali(i.strip())}
    after = t.time()
    print(rv)
    print(after - before)
