""" Ассоциация (агрегация, композиция) """

""" Агрегация """

class Baterry:
    def __init__(self) -> None:
        self. power = 100
        

class Electronic:
        def __init__(self, model, color) -> None:
            self.model = model
            self.color = color
            self.battary = Baterry()
class Phone(Electronic):
    pass
class Laptop(Electronic):
    pass


phone = Phone('Realme', 'Pink')        
bat = Baterry()



""" Композиция """
class Human:
    class Hert:
        def __init__(self) -> None:
            self.heart = '4-хкамерное'

    class Kidneys:
        def __init__(self, q) -> None:
            self.q = q

    class Eyes:
        def __init__(self, color) -> None:
            self.color = color
              

    def __init__(self, q, color) -> None:
        self.heart = self.Hert()
        self.kidneys = self.Kidneys(q)
        self.eyes = self.Eyes(color)



h = Human(2, 'blue')