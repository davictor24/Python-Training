# First, we create the class
class Vector:
    def __init__(self, x, y, z): # Constructor
        # Set properties
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other): # Overload the addition operator
        # Return a Vector object which is the sum of both Vector objects
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other): # Overload the subtraction operator
        # Return a Vector object which is the difference of both Vector objects
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other): # Overload the multiplication operator
        # Return a Vector object which is the cross product of both Vector objects
        # It uses the cross-product formula
        return Vector((self.y * other.z) - (self.z * other.y),
                      (self.z * other.x) - (self.x * other.z),
                      (self.x * other.y) - (self.y * other.x))

    # The __len__ magic method is expected to always return an integer
    # But here, the magnitude of the vector is a float
    # Hence, we can't overload this method for this purpose
    # This was done on purpose, to test your debugging skills ;)
    # If you had an error and you figured this out, great job!
    '''
    def __len__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    '''

    # We define the 'mag' method, to help us find the magnitude
    # This is not a magic method however
    # So we will have to use 'object_name.mag()'
    def mag(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5    


# Get coordinates of vector v1 
print("Vector v1 = (x1)i + (y1)j + (z1)k")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
z1 = float(input("z1 = "))
v1 = Vector(x1, y1, z1) # Create vector object

# Get coordinates of vector v2
print("Vector v2 = (x2)i + (y2)j + (z2)k")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
z2 = float(input("z2 = "))
v2 = Vector(x2, y2, z2) # Create vector object

print("\nv1 = {0}i + {1}j + {2}k".format(x1, y1, z1)) # Print vector v1
print("v2 = {0}i + {1}j + {2}k".format(x2, y2, z2)) # Print vector v2

vs = v1 + v2 # Sum
vd = v1 - v2 # Difference
vp = v1 * v2 # Cross product

# Print results
print("|v1| = " + str(v1.mag()))
print("|v2| = " + str(v2.mag())) 
print("v1 + v2 = {0}i + {1}j + {2}k".format(vs.x, vs.y, vs.z))
print("v1 - v2 = {0}i + {1}j + {2}k".format(vd.x, vd.y, vd.z))
print("v1 x v2 = {0}i + {1}j + {2}k".format(vp.x, vp.y, vp.z))
