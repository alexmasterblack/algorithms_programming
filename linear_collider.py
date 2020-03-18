from collections import deque

def sort_mass(moment_annihilation, time_points, n):
    index = 0
    for i in time_points:
        while index < len(moment_annihilation) and moment_annihilation[index] <= i:
            index = index + 1
        fout.write(str(n - index * 2) + '\n')

fin = open ('linear.in', 'r')            
fout = open ('linear.out', 'w')

n = int(fin.readline())

stack = deque()
coordinates = deque()
moment_annihilation = []

for i in range(n):
    element = fin.readline().split()
    if element[1] == '1':
        stack.append('[')
        coordinates.append(element[0])
    elif element[1] == '-1':
        stack.append(']')
        if len(stack) > 1:
            if stack[-2] == '[' and stack[-1] == ']':
                moment_annihilation.append(abs((int(element[0]) - int(coordinates.pop())) / 2))
                stack.pop()
                stack.pop()
print(moment_annihilation)
stack.clear()
coordinates.clear()
m = int(fin.readline())

time_points = [int(i) for i in fin.read().split()]

moment_annihilation.sort()
sort_mass(moment_annihilation, time_points, n)