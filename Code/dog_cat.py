#!/usr/bin/env python3

class Dog:
    def __init__(self, name):
	self._name = name
    def get_name(self):
	return self._name
    def set_name(self,value):
        self._name = value
    def bark(self):
        print(self.get_name()+ ' is making sound wang wang wang...')

class Cat:
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    def new(self):
        print(self.get_name()+' is making sound miao miao miao...')

dog = Dog('WangCai')
cat = Cat('Kitty')

dog.bark()
cat.new()
