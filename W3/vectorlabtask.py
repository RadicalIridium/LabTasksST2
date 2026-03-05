#don't know why the doc has double comments  ' #"""""" '
#definition of a Simple Vector Class (base code provided by UNI Canberra unit Software Tech 2 (2026))

class Vector:
    #"""Represent a vector in a multidimensional space."""
    def __init__(self, d):
        #"""Create d-dimensional vector of zeros."""
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            self._coords = list(d)
    
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

    #Task 3 !Removed placeholder for __radd__ method!
    def __radd__(self, other):
        if other == 0:
            return self
        return self.__add__(other)

        
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
    
    #Task 4, 5
    def __mul__(self, other):
        #Code for Task 6, Dot product of two vectors
        if isinstance(other, Vector):
            total = 0
            for j in range(len(self)):
                total += self[j] * other[j]
            return total
        
        #Mulitplies the vector with Other
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * other
        return result
        

    
    def __rmul__(self, other):
        return self.__mul__(other)
    

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

'''
#Test code for Task 0
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

#Test code for Task 1
v4 = v1 - v2
print(v4)

#Test code for Task 2
print(-v1)
'''
"""
#test code for Task 3
v1 = Vector(3)
v1[0] = 1
v1[1] = 2
v1[2] = 3

v2 = Vector(3)
v2[0] = 4
v2[1] = 5
v2[2] = 6

print(v1 + v2)

vector = [v1, v2]
total = sum(vector)

#Test code for Task 4, 5
print("___ Task# 4, 5 ___")
print(3 * v1)
print(v1 * 3)

v5 =Vector(3)
v5[0] = 1
v5[1] = 2
v5[2] = 3

print (v5* 10)

# Test code for Task 6
print("___ Task# 6 ___")
print(v1 * v2)
"""

#task 7
v7 = Vector([1, 2, 3])
v8 = Vector(7)
print(v7)
print(v8)