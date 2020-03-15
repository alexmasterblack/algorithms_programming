def merge_mass(mass):
    new_mass=[]
    for i in mass:
      new_mass.extend(i)
    return new_mass

def bucket_sort(mass_words, n):
    if n < 0:
        return mass_words
    else:
        support_mass = [[] for i in range(0, 256)]
        
        for i in range(len(mass_words)):
            letter = mass_words[i]
            for j in range(len(support_mass)):
                if ord(letter[n]) == j:
                    support_mass[j].extend(letter)

        sorted_mass = merge_mass([i for i in support_mass if i != []])
        
        new_sorted_mass = []
        for i in range(0, len(sorted_mass) - 2, 3):
            new_sorted_mass.append([sorted_mass[i], sorted_mass[i + 1], sorted_mass[i + 2]])
        
        return bucket_sort(new_sorted_mass, n - 1)

fin = open ('input.txt', 'r')            
fout = open ('output.txt', 'w')

string = fin.read().splitlines()
del string[0]

sorted_mass = []
for i in bucket_sort(string, 2):
    for j in i:
        sorted_mass.append(j)
        
for i in range(0, len(sorted_mass) - 2, 3):
    fout.write(sorted_mass[i] + sorted_mass[i + 1] + sorted_mass[i + 2] + '\n')
