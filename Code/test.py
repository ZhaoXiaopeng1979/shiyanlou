class Test:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Test:{}'.format(self.name)

t = Test('Python')
print(t)
print(t.name)
