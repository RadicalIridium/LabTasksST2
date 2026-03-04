#don't know why the doc has double comments  ' #"""""" '
#definition of a Simple Vector Class (base code provided by UNI Canberra unit Software Tech 2 (2026))
class Vector:
    #"""Represent a vector in a multidimensional space."""
    def __init__(self, d):
        #"""Create d-dimensional vector of zeros."""
        self._coords = [0]*d
    
    def __len__(self):
        #"""Return the dimension of the vector."""
        return len(self._coords)
    
    def __getitem__(self, j):
        #"""Return jth coordinate of vector."""
        return self._coords[j]
    
    def __setitem__(self, j, value):
        #"""Set jth coordinate of vector to given value"""
        self._coords[j] = value

    def __add__(self, other):
        #"""Return the sum of two vectors"""
        if len(self) != len(other):
            #relies on len method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
            #start with vector of zeros

    #Task 3
    def __radd__(self, other):
        # Treat right-side addition the same as left-side
        # Convert the list to a Vector, then use __add__
        if isinstance(other, list):
            if len(other) != len(self):
                raise ValueError('dimensions must agree')
            temp = Vector(len(other))
            for i in range(len(other)):
                temp[i] = other[i]
            return temp + self
        else:
            return NotImplemented

    #Task 1
    def __sub__(self, other):
        #Return the 'subtraction' of two vectors
        if len(self) != len(other):
            #relies on len method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    #Task 2
    def __neg__(self):
        #Converst a vector to its neg equivilent
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * -1
        return result
    
    #Task 4
    def __rmul__(self, other):
        #Mulitplies the vector with ...
        
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * other[j]
        return result

    def __eq__(self, other):
        #"""Return True if vector has same coordinates as other."""
        return self._coords == other._coords
    
    def __ne__(self, other):
        #"""Return True if vector differs from other."""
        return not self == other
    #rely on existing eq definition

    def __str__(self):
        #"""Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'
    #adapt list representation

v1 = Vector(3)
v2 = Vector(3)

v1[0] = 2
v1[1] = 4
v1[2] = 1

v2[0] = 4
v2[1] = 5
v2[2] = 6

print(v1)
print(v2)

v3 = v1 + v2
print(v3)

v4 = v1 - v2
print(v4)

print(-v1)


v5 =Vector(3)
v5[0] = 1
v5[1] = 2
v5[2] = 3

v5.__rmul__(10)
print (v5)