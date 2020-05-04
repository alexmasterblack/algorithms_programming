fin = open ('input.txt', 'r')            
fout = open ('output.txt', 'w')

first = ' '.join(fin.readline()).split()
second = ' '.join(fin.readline()).split()

support = [[0] * (len(second) + 1) for i in range(len(first) + 1)]
for i in range(1, len(first) + 1):
    for j in range(1, len(second) + 1):
        if first[i - 1] == second[j - 1]:
            support[i][j] = support[i - 1][j - 1] + 1
        else:
            support[i][j] = max(support[i - 1][j], support[i][j - 1])

result = []
i = len(first)
j = len(second)
while i != 0 and j != 0:
    if  first[i - 1] == second[j - 1]:
        result.append(second[j - 1])
        i = i - 1
        j = j - 1
    elif support[i - 1][j] == support[i][j]:
        i = i - 1
    elif support[i][j - 1] == support[i][j]:
        j = j - 1

string = ''
for i in result[::-1]:
    string = string + i

fout.write(string)
