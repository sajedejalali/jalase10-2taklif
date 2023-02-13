class Fraction:
    def __init__(self, s, m):
        self.soorat = s
        self.makhraj = m
    
    def show(self):
        print(self.soorat, "/", self.makhraj )

    def mul(self, f):
        result = Fraction(None, None)
        result.soorat = self.soorat * f.soorat
        result.makhraj = self.makhraj * f.makhraj
        return result
    
    def sum(self, f):
        result = Fraction(None, None)
        result.soorat = (self.soorat * f.makhraj) + (f.soorat * self.makhraj)
        result.makhraj = self.makhraj * f.makhraj
        return result

    def taf(self, f):
        result = Fraction(None, None)
        result.soorat = (self.soorat * f.makhraj) - (f.soorat * self.makhraj)
        result.makhraj = self.makhraj * f.makhraj
        return result

    def tag(self, f):
        result = Fraction(None, None)
        result.soorat = self.soorat * f.makhraj
        result.makhraj = self.makhraj * f.soorat
        return result


a1 = int(input("enter fraction1-soorat : "))
b1 = int(input("enter fraction1-makhraj : "))
a2 = int(input("enter fraction2-soorat : "))
b2 = int(input("enter fraction2-makhraj : "))
while True:    
    print("1- show fractions ")
    print("2- + ")
    print("3- - ")
    print("4- * ")
    print("5- / ")
    print("0- exit")
    op = input("enter your choice : ")
    if op == "1" or op == "show":
        fraction1 = Fraction(a1, b1)
        fraction1.show()
        fraction2 = Fraction(a2, b2)
        fraction2.show()

    if op == "2" or op == "+":
        result_sum = fraction1.sum(fraction2)
        result_sum.show()

    if op == "3" or op == "-":
        result_taf = fraction1.taf(fraction2)
        result_taf.show()

    if op == "4" or op == "*":
        result_mul = fraction1.mul(fraction2)
        result_mul.show()

    if op == "5" or op == "/":
        result_tag = fraction1.tag(fraction2)
        result_tag.show()
    
    if op == "0" or op == "exit":
        break
