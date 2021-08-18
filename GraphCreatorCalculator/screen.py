# https://senablog.com/python-kivy-screen-manager/
# https://atmarkit.itmedia.co.jp/ait/articles/1909/06/news019.html

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from graphcreator import MathGraphCreator

Window.size = (200, 300)

class MainScreen(Screen):
    pass

class AlinearScreen(Screen):

    def __init__(self, **kwargs): 
        super(Screen, self).__init__(**kwargs)
        self.paramDict = {"xmin":0.0, "xmax":0.0, "num":0, "a":0.0, "b":0.0, "c":0.0}

    def pressedExecute(self) -> None:
        self.setParamDict()
        graph = MathGraphCreator(self.paramDict["xmin"], 
                                self.paramDict["xmax"], 
                                self.paramDict["num"], 
                                self.paramDict["a"], 
                                self.paramDict["b"], 
                                self.paramDict["c"])
        graph.createAlinerFunction()

    def setParamDict(self):
        try:
            self.paramDict["xmin"] = float(self.ids.txt_xmin.text[7:])
            self.paramDict["xmax"] = float(self.ids.txt_xmax.text[7:])
            self.paramDict["num"] = int(self.ids.txt_num.text[6:])
            self.paramDict["a"] = float(self.ids.txt_a.text[4:])
            self.paramDict["b"] = float(self.ids.txt_b.text[4:])
        except ValueError:
            pass

class QuadraticScreen(Screen):
    def __init__(self, **kwargs): 
        super(Screen, self).__init__(**kwargs)
        self.paramDict = {"xmin":0.0, "xmax":0.0, "num":0, "a":0.0, "b":0.0, "c":0.0}

    def pressedExecute(self):
        self.setParamDict()
        graph = MathGraphCreator(self.paramDict["xmin"], 
                                self.paramDict["xmax"], 
                                self.paramDict["num"], 
                                self.paramDict["a"], 
                                self.paramDict["b"], 
                                self.paramDict["c"])
        graph.createQuadraticFunction()

    def setParamDict(self):
        try: 
            self.paramDict["xmin"] = float(self.ids.txt_xmin.text[7:])
            self.paramDict["xmax"] = float(self.ids.txt_xmax.text[7:])
            self.paramDict["num"] = int(self.ids.txt_num.text[6:])
            self.paramDict["a"] = float(self.ids.txt_a.text[4:])
            self.paramDict["b"] = float(self.ids.txt_b.text[4:])
            self.paramDict["c"] = float(self.ids.txt_c.text[4:])
        except ValueError:
            pass

class InverseScreen(Screen):
    def __init__(self, **kwargs): 
        super(Screen, self).__init__(**kwargs)   
        self.paramDict = {"xmin":0.0, "xmax":0.0, "num":0, "a":0.0, "b":0.0, "c":0.0}

    def pressedExecute(self):
        self.setParamDict()
        graph = MathGraphCreator(self.paramDict["xmin"], 
                                self.paramDict["xmax"], 
                                self.paramDict["num"], 
                                self.paramDict["a"], 
                                self.paramDict["b"], 
                                self.paramDict["c"])
        graph.createInverseProportional()

    def setParamDict(self):
        # try, except 例外処理 Value : 価値, 値
        try:
            self.paramDict["xmin"] = float(self.ids.txt_xmin.text[7:])
            self.paramDict["xmax"] = float(self.ids.txt_xmax.text[7:])
            self.paramDict["num"] = int(self.ids.txt_num.text[6:])
            self.paramDict["a"] = float(self.ids.txt_a.text[4:])
        except ValueError:
            pass

class ScreenApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(AlinearScreen(name='aline'))
        self.sm.add_widget(QuadraticScreen(name='quard'))
        self.sm.add_widget(InverseScreen(name='inverse'))
        return self.sm


  
