def count_inversions_merge(mass):
    if len(mass) == 1:
        return mass, 0
    else:
        middle_index = len(mass) // 2
        left_mass, left_count = count_inversions_merge(mass[:middle_index:])
        right_mass, right_count = count_inversions_merge(mass[middle_index::])

    sorted_mass = []
    left_i = 0
    right_i = 0
    count = left_count + right_count + 0
    while left_i < len(left_mass) and right_i < len(right_mass):
        if left_mass[left_i] > right_mass[right_i]:
            sorted_mass.append(right_mass[right_i])
            count = count + len(left_mass) - left_i
            right_i = right_i + 1
        else:
            sorted_mass.append(left_mass[left_i])
            left_i = left_i + 1
    
    left_mass = left_mass[left_i::]
    right_mass = right_mass[right_i::]
    if left_mass != []:
        return sorted_mass + left_mass, count
    elif right_mass != []:
        return sorted_mass + right_mass, count

fin = open ('input.txt', 'r')            
fout = open ('output.txt', 'w') 
mass = [int(i) for i in fin.read().split()]
del mass[0]

fout.write(str(count_inversions_merge(mass)[1]))
