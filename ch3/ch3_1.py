inp = input("Enter Input : ")
brackets = {"(":0, "[":0}
unpaired = 0
for ele in inp:
    if ele in brackets:
        brackets[ele] += 1
    if ele == ")":
        if brackets["("] == 0:
            unpaired += 1
        else:
            brackets["("] -= 1
    if ele == "]":
        if brackets["["] == 0:
            unpaired += 1
        else:
            brackets["["] -= 1
for ele in brackets.values():
    unpaired += ele
print(unpaired)
if unpaired == 0:
    print("Perfect ! ! !")
