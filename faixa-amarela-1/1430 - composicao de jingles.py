def verificaNumComp():
    while True:
        x = input("")
        if 3 <= len(x) <= 200:
            break
        elif x == "*":
            break
        print("o valor deve estar entre 3 e 200")
    return x

def verificaCorreto(comp):
    somaCorreto = 0
    valores = [1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64]
    #          w,  h,   q,   e,    s,    t,   x
    x = comp.upper().split('/')
    for i in range(len(x)):
        soma = 0
        for j in range(len(x[i])):
            if (x[i])[j] == 'W':
                soma += valores[0]
            elif (x[i])[j] == 'H':
                soma += valores[1]
            elif (x[i])[j] == 'Q':
                soma += valores[2]
            elif (x[i])[j] == 'E':
                soma += valores[3]
            elif (x[i])[j] == 'S':
                soma += valores[4]
            elif (x[i])[j] == 'T':
                soma += valores[5]
            elif (x[i])[j] == 'X':
                soma += valores[6]
        if soma == 1:
            somaCorreto += 1
    print(somaCorreto)
    
while True:
    comp = verificaNumComp()
    if comp == "*":
        break
    verificaCorreto(comp)
    
