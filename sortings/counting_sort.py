def square(mass):
    new_mass = [0 for i in range(max(mass) + 1)]
    for i in mass:
        new_mass[i] += 1
    for i in range(len(new_mass)):
        if new_mass[i] != 0:
            fout.write((str(i) + ' ') * new_mass[i])

fin = open ('input.txt', 'r')            
fout = open ('output.txt', 'w') 
mass = [int(i) for i in fin.read().split()]
del mass[0]
square(mass)
