print(" *** Summation of each digit ***")
num = input("Enter a positive number : ")
sum = 0
for digit in num:
    digit = int(digit)
    sum += digit
print(f"Summation of each digit =  {sum}")