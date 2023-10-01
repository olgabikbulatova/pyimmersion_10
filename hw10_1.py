# Создайте три (или более) отдельных классов животных.Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
# Вынесите общие свойства и методы классов в класс Животное. Остальные классы наследуйте от него.
# Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Factory:
    def __init__(self, class_name: str, name: str, age: float, spec: str):
        self.class_name = class_name
        self.name = name
        self.age = age
        self.spec = spec

    def create(self):
        anml = eval(f'{self.class_name.title()}("{self.name}", {self.age}, "{self.spec}")')
        return anml


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec


class Dog(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Fish(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Bird(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


dog = Dog('rex', 2, 'run')
fish = Fish('dori', 1, 'salt water')
bird = Bird('hugh', 3, 'stay home')
anml = Factory('dog', 'boy', 5, 'sitdown')
dog2 = anml.create()
anml2 = Factory('fish', 'Ruby', 2, 'fresh water')
fish2 = anml2.create()

for pet in [dog, fish, bird, dog2, fish2]:
    print(pet.get_spec())

