import random

def quick_sort(mass):
    if mass == []:
        return mass
    else:
        sup_elem = random.choice(mass)
        less_sup = [int(i) for i in mass if i < sup_elem]
        more_sup = [int(i) for i in mass if i > sup_elem]
        sup_elem = [int(i) for i in mass if i == sup_elem]
        return quick_sort(less_sup) + sup_elem + quick_sort(more_sup)

fin = open ('input.txt', 'r')            
fout = open ('output.txt', 'w') 
mass = [int(i) for i in fin.read().split()]
del mass[0]
fout.write(str(quick_sort(mass)).replace('[', '').replace(']', '').replace(',', ''))