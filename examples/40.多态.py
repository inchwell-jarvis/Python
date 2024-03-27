# 在 Python 中，多态是通过继承和方法重写来实现的。当子类重写了父类的方法时，可以根据实际情况调用子类的方法，从而实现多态。
#
# 下面是一个简单的示例来说明多态
# ：
class Animal:
    def speak(self):
        """
        定义了一个动物叫声的方法。
        """
        pass


class Dog(Animal):
    def speak(self):
        """
        重写了父类的 speak 方法，实现了狗的叫声。
        """
        return "Woof!"


class Cat(Animal):
    def speak(self):
        """
        重写了父类的 speak 方法，实现了猫的叫声。
        """
        return "Meow!"


# 多态示例
def make_sound(animal):
    """
    接受一个 Animal 类的对象，并调用其 speak 方法，实现多态。
    """
    return animal.speak()


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    # 调用 make_sound 函数，并传入不同的 Animal 类的对象
    print(make_sound(dog))  # 输出：Woof!
    print(make_sound(cat))  # 输出：Meow!

# 在这个示例中：
#
# Animal 类是一个基类，定义了一个 speak() 方法。
# Dog 类和 Cat 类是子类，它们分别重写了 speak() 方法，实现了不同的叫声。
# make_sound() 函数接受一个 Animal 类的对象，并调用其 speak() 方法，实现了多态，即可以根据传入的不同对象调用不同的方法。
# 通过这个示例，展示了多态的概念，即不同对象对同一个消息做出不同的响应。
