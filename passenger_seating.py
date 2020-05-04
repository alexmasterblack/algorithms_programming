modul = 1000000007

fin = open ('input.txt', 'r')            
fout = open ('output.txt', 'w')

n, k = map(int, fin.readline().split())

support = [[0] * (n + 1) for i in range(3)]
support[1][0] = 1

pattern = [0 for i in range(n + 1)]

for i in range(k):
    place = int(fin.readline())
    pattern[place] = 1

print(pattern)
for i in range(1, n + 1):
    support[0][i] = (support[1][i - 1] + support[2][i - 1]) % modul
    if pattern[i] != 1:
        support[1][i] = support[0][i - 1] % modul
        support[2][i] = support[1][i - 1] % modul

fout.write(str((support[0][-1] + support[1][-1]) % modul))
