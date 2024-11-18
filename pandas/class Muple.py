class Muple:
#A wrapper for tuples that gives the illusion of 
#mutability. Hence a "mupple" is a modifiable tuple! :-)

#define the built-in __init()__ method, which every
#class has and which is invoked when an instance
#of the class is instantiated.
    def __init__(self, tuple_data):
        #Validate input
        self.data_type = type(tuple_data).__name__
        if self.data_type != "tuple":
            raise TypeError(f"'{self.data_type}' is not 'tuple'")
            return

        #Assign the provided tuple (or what should be a tuple)
        #to a private instance variable
        self.tuple_data = tuple_data
        #Create list used to give the illusion of mutability
        self.list_data = list(self.tuple_data)
  
    #Implement the __str()__ method for string representation
    #of the muple object.
    def __str__(self):
        muple_len = len(self.list_data)
        return f"'muple({muple_len})'"

    #Implement "private" method to validate index
    def _validate(self, index):
        data_type = type(index).__name__
        if data_type != 'int':
            raise TypeError(f"{index} is not 'int'")
            return False
    
        if index > len(self.list_data) - 1 or index < 0:
            raise IndexError(f"{index} is out of range")
            return False
        return True
  
  
    #Implement method that returns tuple when invoked
    #directly. It is also invoked by other methods
    #that modify the "muple" object.
    def getit(self):
        return tuple(self.list_data)

    #Implement methods for adding, removing, and updating
    #the "muple" object.
    def mappend(self, value):
        #"mappend" - muple append
        self.list_data.append(value)
        return self.getit()

    def mupdate(self, index, value):
        #"mupdate" - muple update
        #If validation fails, an error will be thrown
        if self._validate(index):
            self.list_data[index] = value
            return self.getit()
            
    
    def remove(self, index):
        if self._validate(index):
            self.list_data.pop(index)
            return self.getit()

  
   

