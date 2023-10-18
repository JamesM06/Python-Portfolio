class Cars:
    def __init__(self, name, make, moddle, color):
        self.name = name
        self.make = make
    def __str__(self):
        return f"{self.name}({self.make})"

    
car1 = Cars("car 1", "farari", "S type", "Green")

print(car1.make)
