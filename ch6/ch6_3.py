def gcd(num1, num2):
    return num1 if num2 == 0 else gcd(num2, num1 % num2)

num1, num2 = [int(i) for i in input("Enter Input : ").split()]
if num2 > num1:
    num1, num2 = num2, num1
if num1 == 0 and num2 == 0:
    print("Error! must be not all zero.")
else:
    print(f"The gcd of {num1} and {num2} is : {abs(gcd(num1, num2))}")