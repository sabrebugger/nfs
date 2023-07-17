from collections import Counter

s = list(map(lambda x: x.strip(), open('input.txt').readlines()))
print(s)
for el in s:
    c = Counter(el)
    print(c)
    print(max(c, key=lambda x: c[x]))
