from collections import Counter
from dz import vvod

els = vvod(input())
ans = Counter(els)
print('Элемент | Частота')
print(*[f'{i} | {ans[i]}' for i in ans], sep='\n')
