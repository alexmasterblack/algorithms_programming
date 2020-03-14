def merge_sort(left_mass, right_mass):
    sorted_mass = []
    left_i = 0
    right_i = 0
    while left_i < len(left_mass) and right_i < len(right_mass):
        if left_mass[left_i] < right_mass[right_i]:
            sorted_mass.append(left_mass[left_i])
            del left_mass[0]
        else:
            sorted_mass.append(right_mass[right_i])
            del right_mass[0]
    if left_mass != []:
        return sorted_mass + left_mass
    elif right_mass != []:
        return sorted_mass + right_mass
    
def merge_partition(mass):
    if len(mass) == 1:
        return mass
    else:
        middle_index = len(mass) // 2
        left_mass = merge_partition(mass[:middle_index:])
        right_mass = merge_partition(mass[middle_index::])
        return merge_sort(left_mass, right_mass)

fin = open ('input.txt', 'r')            
fout = open ('output.txt', 'w') 
mass = [int(i) for i in fin.read().split()]
del mass[0]

fout.write(str(merge_partition(mass)).replace('[', '').replace(']', '').replace(',', ''))