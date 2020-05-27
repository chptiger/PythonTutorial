class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal): # class Dog inheritance all methods from Mammal
    pass # do not worry about it


class Cat(Mammal):
    def walk(self):
        print("cat walk")
    def be_annoyihng(self):
        print("cat annoying")


dog = Dog()
dog.walk()
cat = Cat()
cat.walk()
cat.be_annoyihng()