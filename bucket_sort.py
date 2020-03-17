def merge_mass(mass):
    new_mass=[]
    for i in mass:
      new_mass.extend(i)
    return new_mass

def join_mass(mass):
    new_mass = []
    for i in range(0, len(mass) - 2, 3):
        new_mass.append([mass[i], mass[i + 1], mass[i + 2]])
    return new_mass
    

def bucket_sort(mass_words, n):
    if n < 0:
        return mass_words
    else:
        
        support_mass = [[] for i in range(123)]
        for i in range(len(mass_words)):
            letter = mass_words[i]
            support_mass[ord(letter[n])].append(letter)
        
        sorted_mass = merge_mass([i for i in support_mass if i != []])
        
        return bucket_sort(sorted_mass, n - 1)

fin = open ('input.txt', 'r')            
fout = open ('output.txt', 'w')

string = fin.read().splitlines()
del string[0]

new_string = []
for i in string:
    new_string.append([j for j in i])

sorted_mass = []
for i in bucket_sort(new_string, 2):
    for j in i:
        sorted_mass.append(j)

for i in join_mass(sorted_mass):
    fout.write(''.join(i) + '\n')
