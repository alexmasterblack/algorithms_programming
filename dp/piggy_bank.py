infinity = 10010

fin = open ('input.txt', 'r')            
fout = open ('output.txt', 'w')

e, f, n = map(int, fin.readline().split())
coins_weight = f - e

support = [infinity for i in range(coins_weight + 1)]
support[0] = 0

for i in range(n):
    c, w = map(int, fin.readline().split())
    for j in range(1, coins_weight + 1):
        if j >= w:
            support[j] = min(support[j], support[j - w] + c)

if support[-1] == infinity:
    fout.write('-1')
else:
    fout.write(str(support[-1]))
