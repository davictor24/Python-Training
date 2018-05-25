class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mag(self):
        return ((self.x)**2 + (self.y)**2) ** 0.5

    def __add__(self, other):
        vector_sum = Vector2D(self.x + other.x, self.y + other.y)
        return vector_sum

vectorA = Vector2D(3, 4)
vectorB = Vector2D(2, -1)
vectorC = vectorA + vectorB

print("x coordinate: " + str(vectorC.x))
print("y coordinate: " + str(vectorC.y))

