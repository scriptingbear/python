#implement a list which prints out its members in reverse order

class RList:
    def __init__(self, some_list):
        self.some_list = some_list
        self.current_index = len(self.some_list) - 1
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current_index < 0:
            raise StopIteration
        else:
            self.current_index -=1
            return self.some_list[self.current_index + 1]
    

print("Normal list:")
my_list = [1,2,3,4,5]
for item in my_list:
    print(item)
    
print("Reversed list:")  

my_rlist = RList([1,2,3,4,5])
for item in my_rlist:
    print(item)
