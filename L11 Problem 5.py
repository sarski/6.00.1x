class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def __len__(self):
        """Returns the number of elements in self """
        return len(self.vals)

    def intersect(self, other):
        """Returns a new intSet containing elements that appear in both sets."""
        assert type(self) == type(other)
        newIntSet = intSet()
        idx1 = 0
        idx2 = 0
        while (idx1 < len(self.vals) and idx2 < len(other.vals)):
            if self.vals[idx1] == other.vals[idx2]:
                newIntSet.insert(self.vals[idx1])
                idx1 += 1
                idx2 += 1
            elif self.vals[idx1] < other.vals[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return newIntSet