fin = open ('input.txt', 'r')     
fout = open ('output.txt', 'w')

mass = [int(i) for i in fin.read().split()]
del mass[0]

new_mass = [0 for i in range(101)]
for i in range(0, len(mass) - 1, 2):
    for j in range(mass[i] - mass[i + 1], mass[i] + mass [i + 1]):
        if j < 0:
            continue
        new_mass[j] = new_mass[j] + 1
        if j == 100:
            break

fout.write(str(max(new_mass)))
