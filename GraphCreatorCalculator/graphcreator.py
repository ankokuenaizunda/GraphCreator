# https://qiita.com/mookouchi/items/5694d7e3c7b6a181f169

import matplotlib.pyplot as plt
import numpy as np
from calculator import CalcMath

class MathGraphCreator():
    np_obj = np
    plt_obj = plt

    def __init__(self, xMin, xMax, interval, a, b, c):
        super().__init__
        self.xMin = xMin
        self.xMax = xMax
        self.num = interval
        self.calc_obj = CalcMath(a, b, c)

    # 一次関数のグラフを描画する。
    def createAlinerFunction(self):
        x = self.np_obj.linspace(self.xMin, self.xMax, self.num)
        y = self.calc_obj.calculateAlinerFunction(x)
        self.plt_obj.plot(x, y)

        self.plt_obj.axhline(0, linewidth=2, color="gray")
        self.plt_obj.axvline(0, linewidth=2, color="gray")
        self.plt_obj.xlabel('X-axis')
        self.plt_obj.ylabel('Y-axis')
        self.plt_obj.grid(True)
        self.plt_obj.show()
    
    # 二次関数のグラフを描画する。
    def createQuadraticFunction(self):
        x = self.np_obj.linspace(self.xMin, self.xMax, self.num)
        y = self.calc_obj.calculateQuadraticFunction(x)
        self.plt_obj.plot(x, y)

        self.plt_obj.axhline(0, linewidth=2, color="gray")
        self.plt_obj.axvline(0, linewidth=2, color="gray")
        self.plt_obj.xlabel('X-axis')
        self.plt_obj.ylabel('Y-axis')
        self.plt_obj.grid(True)
        self.plt_obj.show()

    # 反比例のグラフを描画する。
    def createInverseProportional(self):
        x = self.np_obj.linspace(self.xMin, self.xMax, self.num)
        y = self.calc_obj.calculateInverseProportional(x)
        self.plt_obj.plot(x, y)

        self.plt_obj.axhline(0, linewidth=2, color="gray")
        self.plt_obj.axvline(0, linewidth=2, color="gray")
        self.plt_obj.xlabel('X-axis')
        self.plt_obj.ylabel('Y-axis')
        self.plt_obj.grid(True)
        self.plt_obj.show()

