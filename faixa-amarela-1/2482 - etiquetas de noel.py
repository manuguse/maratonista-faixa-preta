def verificaNum():
    while True:
        x = int(input())
        if 1 <= x <= 100:
            break
    return x
    
lingua = []
traducao = []

n = verificaNum()

for i in range(n):
    lingua.append(input())
    traducao.append(input())

m = verificaNum()

for i in range(m):
    nome = input()
    lang = input()
    for j in range (len(lingua)):
        if lang == lingua[j]:
            mensagem = traducao[j]
    
    print(nome)
    print(mensagem)
    print('')
