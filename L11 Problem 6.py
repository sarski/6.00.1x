class Queue(object):
    """A Queue is a list of elements the follows the FIFO method of removing
    elements"""
    def __init__(self):
        """Create an empty queue"""
        self.vals = []
        
    def insert(self, e):
        """Inserts one element in the queue"""
        self.vals.append(e)
        
    def remove(self):
        """Removes the first element in the queue and returns the value. 
        Raises a ValueError if the queue is empty"""
        try:
            return self.vals.pop(0)
        except:
            raise ValueError('Queue is empty')