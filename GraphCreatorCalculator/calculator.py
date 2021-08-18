class CalcMath():
    def __init__(self ,a, b, c):
        self.a = a
        self.b = b
        self.c = c
        pass

    # 一次関数の計算
    def calculateAlinerFunction(self, x):
        return self.a * x + self.b

    # 二次関数の計算
    def calculateQuadraticFunction(self, x):
        return self.a*(x**2) + self.b*x + self.c

    # 反比例の計算
    def calculateInverseProportional(self, x):
        return self.a/x

    #def calculateSquare(self, vertical, beside):
    #    s = vertical * beside
    #    return s
#
    #def calculateTriangle(self, bottom, height):
    #    s = bottom * height * 1/2
    #    return s
#
    #def calculateTrapezoid(self, upper, bottom, height):
    #    s = (upper + bottom) * height * 1/2
    #    return s

