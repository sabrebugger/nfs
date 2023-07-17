file = None
with open('input.txt', 'r', encoding="utf-8") as f:
    file = f.readlines()
n = int(file[0]) # int(input())
posadka = [el.strip() for el in file[1:n + 1]] #[input() for _ in range(n)]
m = int(file[n + 1]) #int(input())
d = {
    0: 'A', 1: "B", 2: "C", 4: "D", 5: "E", 6: "F"
}
for k in range(m):
    num, side, pos = file[k + n + 2].strip().split()#input().split()
    num = int(num)
    have_seats = False
    for i in range(n):
        t = posadka[i].split('_')
        if pos == 'aisle':
            if side == 'left' and t[0][3 - num:] == '.' * num:
                t[0] = t[0][:3 - num] + 'X' * num
            elif side == "right" and t[1][:num] == '.' * num:
                t[1] = 'X' * num + t[1][num:]
        elif pos == 'window':
            if side == 'left' and t[0][:num] == '.' * num:
                t[0] = 'X' * num + t[0][num:]
            elif side == "right" and t[1][3 - num:] == '.' * num:
                t[1] = t[1][:3 - num] + 'X' * num
        posadkai = t[0] + '_' + t[1]
        if 'X' in posadkai:
            seats = []
            for j in range(len(posadkai)):
                if posadkai[j] == 'X':
                    seats.append(str(i + 1) + d[j])
            print('Passengers can take seats: %s' % ' '.join(seats))
            print('\n'.join(posadka[:i] + [posadkai] + posadka[i + 1:]))
            have_seats = True
            posadka[i] = posadkai.replace('X', '#')
            break
    if not have_seats:
        print('Cannot fulfill passengers requirements')
