"""
類!
建構函數固定用 def __init__(self) ，第一個固定是self，後面可跟任意數量的參數
"""


class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    def say_hello(self):
        print(self.name + "喵喵")


cuteCat = Cat("大橘喵", 3)
print(cuteCat.name + str(cuteCat.age) + "歲")
cuteCat.say_hello()
