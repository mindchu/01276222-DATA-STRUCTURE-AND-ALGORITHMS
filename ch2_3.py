def RANGE(*args):
    max_decimal = 0
    for i in args:
        s = str(i)
        count = len(s.split('.')[-1])
        if max_decimal < count:
            max_decimal = count
    result = list()
    if len(args) == 1:
        i = 0.0
        while i < args[0]:
            result.append(round(i, max_decimal))
            i += 1.0
    elif len(args) == 2:
        i = args[0]
        while i < args[1]:
            result.append(round(i, max_decimal))
            i += 1.0
    else:
        i = args[0]
        while i < args[1]:
            result.append(round(i, max_decimal))
            i += args[2]
    return tuple(result)

print('*** New Range ***')
n = [float(i) for i in input('Enter Input : ').split()]
if len(n) == 1:
    k = RANGE(n[0])
    print(RANGE(n[0]))
elif len(n) == 2:
    print(RANGE(n[0], n[1]))
elif len(n) == 3:
    print(RANGE(n[0], n[1], n[2]))