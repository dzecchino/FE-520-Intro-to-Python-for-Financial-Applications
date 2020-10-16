class RectangularCoordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Distance(self):
        return ((self.x**2)+(self.y**2))**(1/2)

if __name__ == "__main__":
    d = RectangularCoordinate(3, 3)
    print(d.Distance())                 #used to test the code

    d = RectangularCoordinate(3, 4)     #used to test the code
    print(d.Distance())
