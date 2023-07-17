from collections import Counter

n = ''.join([el.strip() for el in open("input.txt", 'r')]).replace(' ', '')
c = Counter(n)
ans = sorted(Counter(n))
m = max(c.values())
for i in range(m):
    s = ''
    for el in ans:
        if i >= m - c[el]:
            s += '#'
        else:
            s += ' '
    print(s)
print(''.join(ans))
