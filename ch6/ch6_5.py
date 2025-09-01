def staircase(n, current=0):
    if n == 0:
        return "Not Draw!"
    if current == abs(n) - 1:
        return "_" * current + "#" * (abs(n) - current)
    line = "_" * current + "#" * (abs(n) - current)
    if n > 0:
        return staircase(n, current + 1) + "\n" + line
    else:
        return line + "\n" +  staircase(n, current + 1)
    

print(" *** Stair case ***")
print(staircase(int(input("Enter Input : "))))
print("===== End of program =====")