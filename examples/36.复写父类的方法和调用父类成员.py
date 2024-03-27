class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """
        定义了一个动物叫声的方法。
        """
        return "Generic animal sound"


class Dog(Animal):
    def __init__(self, name, breed):
        """
        Dog 类继承了 Animal 类，并在初始化时接受名称和品种两个参数。
        """
        super().__init__(name)  # 调用父类的构造函数，初始化名称
        self.breed = breed

    def speak(self):
        """
        重写了父类的 speak 方法，以实现狗的叫声。
        """
        return "Woof!"

    def full_speak(self):
        """
        定义了一个方法，该方法调用了父类的 speak 方法，并加上了品种信息。
        """
        return f"{super().speak()} I'm a {self.breed}."


if __name__ == "__main__":
    dog = Dog("Buddy", "Golden Retriever")
    print(dog.speak())  # 输出：Woof!
    print(dog.full_speak())  # 输出：Generic animal sound I'm a Golden Retriever.
