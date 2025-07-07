def odd_list(al):
    odd_num = []
    for num in al:
        if num % 2 != 0:
            odd_num.append(num)
    return odd_num

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)