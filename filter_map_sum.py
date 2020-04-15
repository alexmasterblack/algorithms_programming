def check(i):
    if i % 9 == 0:
        return 1
    else:
        return 0

print(sum(map(lambda i: i**2, filter(check, range(10,100)))))

print(sum(map(lambda i: i**2, filter(lambda i: i % 9 == 0, range(10,100)))))