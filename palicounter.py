import time as t
from pprint import pprint


def pali(s):
    if s == s[::-1]:
        return True
    else:
        return False


before = t.time()
with open('foo.txt') as f:
    rv = {i.strip() for i in f if pali(i.strip())}
    after = t.time()
    pprint(rv, compact=True)
    print(after - before)
