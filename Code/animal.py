#!/usr/bin/env python3
class Animal:
    owner = 'Jack'
    def __init__(self, name):
        self._name = name
    @classmethod
    def get_owner(cls):
        return cls.owner

    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(self.get_name()+' is making sound wang wang wang...')

class Cat(Animal):
    def make_sound(self):
        print(self.get_name()+' is making sound miu miu miu ...')

dog = Dog('WangCai')
cat = Cat('Kitty')
dog.make_sound()
cat.make_sound()

print("Above all are owned {}".format(Animal.owner))
print("All cats' owner is {}".format(Cat.owner))
print("There is only one owner:{}".format(Animal.get_owner()))
