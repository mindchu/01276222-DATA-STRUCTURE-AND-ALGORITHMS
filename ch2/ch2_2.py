class Spherical:
    def __init__(self,r):
        self.radius = r

    def changeR(self,Radius):
        self.radius = Radius

    def findVolume(self):
        return (4/3) * PI * self.radius**3

    def findArea(self):
        return 4 * PI * self.radius**2

    def __str__(self):
        return "Radius =" + str(self.radius) + " Volumn = " + str(self.findVolume()) + " Area = " + str(self.findArea())

r1, r2 = input("Enter R : ").split()
PI = 3.141592653589793
R1 = Spherical(int(r1))
print(type(R1))
print(R1)
R1.changeR(int(r2))
print(R1)