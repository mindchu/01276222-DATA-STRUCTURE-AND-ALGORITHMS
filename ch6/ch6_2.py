def length(txt):
    def loop(char, index = 0):
        try:
            _ = char[index]
            print(char[index], end="")
            print("*" if index % 2 == 0 else "~", end="")
            return 1 + loop(char, index + 1)
        except IndexError:
            return 0
    return loop(txt)
print(" *** Length of string (Recursion) ***")
inp = input("Enter Input : ")
print(f"\nlength of '{inp}' is {length(inp)}")