class Calc:
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a / b
    def true_div(self, a, b):
        return a // b
    def mod(self, a, b):
        return a % b
    def divmod(self, a, b):
        return self.true_div(a,b),self.div(a,b) 
    def pow(self, a, b):
        return a ** b
    def sqrt(self, a, ndigits=2):
        import math
        sqrt_num = math.sqrt(a)
        return round(sqrt_num, ndigits)
    def percent(self, total, __percent):
        return (total + __percent)/100
ertay = Calc()
