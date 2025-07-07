class translator:
    def __init__(self):
        self.check_dict = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }

    def deciToRoman(self, num):
        result = ""
        for roman, value in self.check_dict.items():
            while num >= value:
                result += roman
                num -= value
        return result

    def romanToDeci(self, s):
        index = 0
        total = 0
        while index < len(s):
            if index + 1 < len(s) and s[index:index + 2] in self.check_dict:
                total += self.check_dict[s[index:index + 2]]
                index += 2
            else:
                total += self.check_dict[s[index]]
                index += 1
        return total 

print(" *** Decimal to Roman ***")
num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))