while True:
    n = int(input())
    if 2 <= n <= 64:
        break
primeira = input().split(' ')
y = len(primeira)

for i in range(y-1):
    proximaFila = []
    for j in range(y-1):
        if primeira[j] != primeira[j + 1]:
            proximaFila.append("-1")
        else:
            proximaFila.append("1")
    y -= 1
    primeira = proximaFila[:]

if proximaFila[0] == "1":
    print('preta')
else:
    print('branca')
