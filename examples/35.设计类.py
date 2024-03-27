# 设计一个类
class Student:
    name1 = None
    name2 = None
    name3 = None
    name4 = None


# 创建一个对象
stu1 = Student()

# 对对象进行赋值
stu1.name1 = '赵鸿飞'
stu1.name2 = '朱帅帅'
stu1.name3 = '葛兴兴'
stu1.name4 = '王娇娇'

# 输出
print(stu1.name1)
print(stu1.name2)
print(stu1.name3)
print(stu1.name4)


# class 类名称:
#     类属性=''   // 类的变量
#     类属性=''   // 类的变量
#     类属性=''   // 类的变量
#     类属性=''   // 类的变量
#
#     类的行为    // 类的函数
#     类的行为    // 类的函数


class Jarvis:
    name = 'Downey'

    def get_name(self):
        print(self.name)

    def change_name(self, msg):
        print(msg)


Jarvis_1 = Jarvis()
Jarvis_1.get_name()
Jarvis_1.change_name(123)


# 构造方法
class JarvisS1:
    name = None
    age = None
    tel = None

    # 如果写了 __init__ 不需要写这几个声明了
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel


JarvisS11 = JarvisS1('赵鸿飞', 18, 17856222886)
print(JarvisS11.name)
print(JarvisS11.age)
print(JarvisS11.tel)


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """
        这是一个抽象方法，子类需要重写该方法来实现特定的动物叫声。
        """
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        """
        重写了父类的speak方法，以实现狗的叫声。
        """
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        """
        重写了父类的speak方法，以实现猫的叫声。
        """
        return f"{self.name} says Meow!"


if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    print(dog.speak())  # 输出：Buddy says Woof!
    print(cat.speak())  # 输出：Whiskers says Meow!








class Flyable:
    def fly(self):
        """
        定义了一个飞行的方法。
        """
        return "Flying high"


class Swimmable:
    def swim(self):
        """
        定义了一个游泳的方法。
        """
        return "Swimming gracefully"


class Bird(Flyable, Swimmable):
    def __init__(self, name):
        """
        Bird 类继承了 Flyable 和 Swimmable 两个父类，并在初始化时接受一个名称参数。
        """
        self.name = name

    def speak(self):
        """
        定义了一个鸟类特有的叫声方法。
        """
        return f"{self.name} says Chirp!"


if __name__ == "__main__":
    bird = Bird("Sparrow")

    print(bird.fly())  # 输出：Flying high
    print(bird.swim())  # 输出：Swimming gracefully
    print(bird.speak())  # 输出：Sparrow says Chirp!


