class Fraction:
    def __init__(self, numerator, denuminator):
        self.numerator = numerator
        self.denuminator = denuminator
        self.simplify()

    def sum(self, other_fraction):
        numerator = self.numerator * other_fraction.denuminator + self.denuminator * other_fraction.numerator
        denuminator = self.denuminator * other_fraction.denuminator
        return Fraction(numerator, denuminator) 
    
    def mul(self, other_fraction):
        numerator = self.numerator * other_fraction.numerator
        denuminator = self.denuminator * other_fraction.denuminator
        return Fraction(numerator, denuminator)

    def sub(self, other_fraction):
        numerator = self.numerator * other_fraction.denuminator - self.denuminator * other_fraction.numerator
        denuminator = self.denuminator * other_fraction.denuminator
        return Fraction(numerator, denuminator)        
    
    def div(self, other_fraction):
        numerator = self.numerator * other_fraction.denuminator
        denuminator = self.denuminator * other_fraction.numerator
        return Fraction(numerator, denuminator)        
    
    def to_number(self):
        return self.numerator / self.denuminator
    
    def show(self):
        print(self.numerator, "/", self.denuminator)
    
    def simplify(self):
        min = self.numerator if self.numerator < self.denuminator else self.denuminator
        for i in range(int(min), 1, -1):
            if self.numerator % i == 0 and self.denuminator % i == 0:
                self.numerator = int(self.numerator / i)
                self.denuminator = int(self.denuminator / i)
                break

##### TEST CASE #####
a = Fraction(22, 4)
b = Fraction(7, 5)
print("simplified a = ", end=" ")
a.show()
print("simplified b = ", end="")
b.show()
print("sum: ", end="")
a.sum(b).show()
print("sub: ", end="")
a.sub(b).show()
print("mul: ", end="")
a.mul(b).show()
print("div: ", end="")
a.div(b).show()
print(f"Number of a: {a.to_number()}")
print(f"Number of b: {b.to_number()}")
