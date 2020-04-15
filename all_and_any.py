n_of_groups = int(input())

base = []
for i in range(n_of_groups):
    n_of_students = int(input())
    dictionary = {}
    for j in range(n_of_students):
        surname, count = input().split()
        dictionary[surname] = int(count)
    base.append(dictionary)

info = []
for i in base:
    if any(elem[1] > 1 for elem in i.items()):
        info.append(True)
    else:
        info.append(False)

if all(info) == False:
    print('НЕТ')
elif all(info) == True:
    print('ДА')