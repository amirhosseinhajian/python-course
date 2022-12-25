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
