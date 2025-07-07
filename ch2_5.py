class funString():

    def __init__(self,string = ""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self) :
        return len(self.string)

    def changeSize(self):
        result = ""
        for s in self.string:
            if 'A' <= s <= 'Z':
                result += chr(ord(s) + 32)
            elif 'a' <= s <= 'z':
                result += chr(ord(s) - 32)
            else:
                result += s
        return result

    def reverse(self):
        result = ""
        for s in self.string[::-1]:
            result += s
        return result

    def deleteSame(self):
        result = ""
        for s in self.string:
            if s not in result:
                result += s
        return result

str1, str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())
elif str2 == "2":  print(res.changeSize())
elif str2 == "3" : print(res.reverse())
elif str2 == "4" : print(res.deleteSame())