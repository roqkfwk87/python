class Bag:
    count = 0
    
    def __init__(self):
        Bag.count += 1

    @classmethod
    def sell(cls):
        cls.count -= 1

    def sell_any():
        Bag.count -= 1

    @classmethod
    def remain_bag(cls):
        return cls.count
    
print(f"현재 가방: {Bag.remain_bag()}개")

bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
bag4 = Bag()
bag5 = Bag()

print(f"현재 가방: {Bag.remain_bag()}개")

bag1.sell()
bag2.sell()
Bag.sell()
Bag.sell_any()

print(f"현재 가방: {Bag.remain_bag()}개")

