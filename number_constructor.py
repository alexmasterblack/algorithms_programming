fin = open ('input.txt', 'r')            
fout = open ('output.txt', 'w')

n = int(fin.readline())
pattern = fin.readline()

support = [[0] * (n + 1) for i in range(10)]

for i in range(n):
    if pattern[i] == '*':
        for j in range(10):
            for q in range(10):
                if j != q:
                    support[q][i + 1] = max(support[q][i + 1], support[j][i] + j * q)
    else:
        element = int(pattern[i])
        for q in range(10):
            if q == element:
                result = 0
            else:
                result = element * q
            support[q][i + 1] = max(support[q][i + 1], support[element][i] + result)
        
        for j in range(10):
            if j != element:
                support[j][i] = 0

for i in support:
    print(*i)
fout.write(str(8 * 9 * (n - 1) - support[0][-1]))
