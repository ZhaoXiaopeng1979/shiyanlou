#!/usr/bin/env python3

class A:
    @property
    def action(self):
        return self._what

    @action.setter
    def action(self, value):
        self._what = value

a = A()
a.action = 'Swim'
print(a.action)

b = A()
b.action = 9999
print(b.action)
