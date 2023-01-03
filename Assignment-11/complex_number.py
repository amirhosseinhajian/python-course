class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image
    
    def show(self):
        print(self.real, f"{'+ ' if self.image >= 0 else '- '}{abs(self.image)}", "i")

    def sum(self, other):
        return Complex(self.real + other.real, self.image + other.image)
    
    def sub(self, other):
        return Complex(self.real - other.real, self.image - other.image)
    
    def mul(self, other):
        return Complex(self.real * other.real - self.image * other.image, self.real * other.image + self.image * other.real)

##### TEST CASE #####
a = Complex(2, 7)
b = Complex(5, 6)
print("a = ", end=" ")
a.show()
print("b = ", end=" ")
b.show()
print("sum:", end=" ")
a.sum(b).show()
print("sub:", end=" ")
a.sub(b).show()
print("mul:", end=" ")
a.mul(b).show()
