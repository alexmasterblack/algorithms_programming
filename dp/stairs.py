fin = open ('input.txt', 'r')            
fout = open ('output.txt', 'w')

n = int(fin.readline())
stairs = list(map(int, fin.read().split()))

stairs.insert(0, 0)

if n == 1:
    fout.write(str(stairs[1]))
else:
    for i in range(2, n + 1):
        stairs[i] = max(stairs[i - 1], stairs[i - 2]) + stairs[i]
    fout.write(str(stairs[-1]))
