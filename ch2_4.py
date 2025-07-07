def sum_zero(args):
    result = []
    total_num = len(args)

    for i in range(total_num - 2):
        for j in range(i + 1, total_num - 1):
            for k in range(j + 1, total_num):
                if args[i] + args[j] + args[k] == 0 and \
                    [args[i], args[j], args[k]] not in result:
                        result.append([args[i], args[j], args[k]])
    return result

args = [int(i) for i in input("Enter Your List : ").split()]
if len(args) < 3:
    print("Array Input Length Must More Than 2")
else:
    print(sum_zero(args))
