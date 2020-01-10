
class Variable:
    def __init__(self, name, shapes, value=None):
        self.memberships = {}
        self.name = name
        self.value = value
        self.shapes = shapes

    def fuzzify(self):
        for shape in self.shapes.values():
            self.memberships[shape.name] = shape.membership(self.value)
