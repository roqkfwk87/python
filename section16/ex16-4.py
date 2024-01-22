class Coffee:
    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self):
        print(f"원두: {self.bean}")

class Espresso(Coffee):
    def __init__(self, bean, water):
        super().__init__(bean)
        self.water = water

    def espresso_info(self):
        super().coffee_info()
        print(f"물: {self.water}ml")

coffee = Espresso("콜롬비아", 30)
coffee.espresso_info()