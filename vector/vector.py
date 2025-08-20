
"""“To implement all comparison operator overloads (as explained on page 76 of the Python book),
 we only need to define __eq__ along with one other comparison method (e.g., __lt__) while
 using the functools.total_ordering decorator.”"""

from functools import total_ordering

@total_ordering
class Vectors:
    def __init__(self, d=1): #default dimension value
        if isinstance(d, int):
            self._coords= [0]*d
        elif isinstance(d, str): #for d="3"
             d = self.dimension_validation(d)
             self._coords= [0]*d
        elif  isinstance(d, Vectors):
            self._coords = d._coords[:] #copy constructor with  deep copy
        else:
            raise TypeError("unnmatched dimension type")
        
    def dimension_validation(self, d):
        if d.isdigit():
            return int(d)
        raise ValueError("String dimension must contain digits only")  

    def __len__(self):
        return len(self._coords)    
        
    def __getitem__(self, j):
        return self._coords[j]
     
    def __setitem__(self, j, value):  
        try:        
         if isinstance(value, (int, float)):
            self._coords[j] = value      
         elif isinstance(value, str):
            value = self.item_validation(value)  
            self._coords[j] = value
         else:
            raise TypeError("value type is unmatched")
         
        except IndexError:
            raise IndexError("index out of bound")
        
    def item_validation(self, value):
            if value.isdigit():
                return int(value) 
            raise ValueError("item should be digit")  
           
    def __add__(self, other):
        if not isinstance(other, Vectors):
            raise TypeError("Can only add another Vectors instance")

        if len(self._coords) == len(other._coords):
            result = Vectors(len(self._coords))
            for j in range(len(self._coords)):
             result[j] = self._coords[j] + other._coords[j]  
            return result

        else:
            raise ValueError("unmatched vectors dimensions")  
       


    def __eq__(self, other):
        if not isinstance(other, Vectors):
            return False
        return self._coords == other._coords

    def __lt__(self, other):
        if not isinstance(other, Vectors):
            raise TypeError("Comparison only supported between Vectors")
        return self._coords < other._coords
    
    def __str__(self):
        return "<" + str(self._coords)[1:-1] + ">"
    
    @property
    def dimension(self):
        """Return the dimension of the vector"""
        return len(self._coords)
    
    @property
    def coords(self):
        """Return a safe copy of coordinates (protect encapsulation)"""
        return  self._coords[:] 