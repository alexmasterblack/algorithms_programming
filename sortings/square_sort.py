def selection_sort(mass):
    for i in range(len(mass)):
        elem = mass.index(min(mass[i::]), i)
        mass[i], mass[elem] = mass[elem], mass[i]
    return mass

fin = open ('input.txt', 'r')            
fout = open ('output.txt', 'w') 
mass = [int(i) for i in fin.read().split()]
del mass[0]
fout.write(str(selection_sort(mass)).replace('[', '').replace(']', '').replace(',', ''))
