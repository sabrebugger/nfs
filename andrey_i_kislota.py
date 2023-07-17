n = int(input())
l = [int(el) for el in input().split()]
temp = l[0]
ans = 0
for el in l:
    if el > temp:
        ans += el - temp
        temp = el
    elif el < temp:
        ans = -1
        break
print(ans)
