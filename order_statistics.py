import random

def search_sup_index(mass):
    sup_index = random.randint(0, len(mass) - 1) 
    sup_elem = mass[sup_index]
    mass[sup_index], mass[len(mass) - 1] = mass[len(mass) - 1], mass[sup_index]
    
    index = -1
    for i in range(0, len(mass)):
        if mass[i] <= sup_elem:
            index = index + 1
            mass[i], mass[index] = mass[index], mass[i]
    return index

def statistics(mass, k):
    if len(mass) == 1:
        return mass[0]
    else:
        sup_index = search_sup_index(mass)
        if k == sup_index:
            return mass[sup_index]
        elif k > sup_index:
            return statistics(mass[sup_index + 1::], k - sup_index - 1)
        else:
            return statistics(mass[:sup_index:], k)

fin = open ('input.txt', 'r')            
fout = open ('output.txt', 'w')
k = [int(i) for i in fin.readline().split()]
mass = [int(i) for i in fin.read().split()]

fout.write(str(statistics(mass, k[1] - 1)).replace('[', '').replace(']', '').replace(',', ''))
