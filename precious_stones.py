'''
Write an object oriented program to create a precious stone.
Not more than 5 precious stones can be held in possession at a
given point of time. If there are more than 5 precious stones,
delete the first stone and store the new one.
'''

class Stone:
    _stones = []
    _limit = 5

    def __init__(self, name):
        Stone.addStone(name)
        Stone.displayStones()    
 
    def getLimit():
        return Stone._limit

    def setLimit(value):
        if value < 1:
            Stone._limit = 5
        else:
            Stone._limit = value

    
    def addStone(name):
        #if _stones is too big we must truncate it to size
        
        if len(Stone._stones) > Stone._limit:
            print("Removing last {0} items from list of stones because it exceeds the limit of {1}." \
                  .format(len(Stone._stones) - Stone._limit, Stone._limit))
            Stone._stones = Stone._stones[:Stone._limit]
   
            
        if len(Stone._stones) == Stone._limit:
            #can't have more than the limit of stones
            #delete first stone and then add
            #new stone to list
            deleted_stone = Stone._stones[0]
            del Stone._stones[0]
            print("=" * 20)
            print("{} stone limit reached".format(Stone._limit))
            print("Deleted first stone \"{}\"".format(deleted_stone))
            print("=" * 20)
            
        Stone._stones.append(name)
        print("Added new stone \"{}\"".format(name))

    
    def displayStones():
        print(Stone._stones)



stone_names = ["diamond",
               "onyx",
               "topaz",
               "opal",
               "lapis lazuli",
               "emerald",
               "sapphire"]

#try to create 7 stones, regardless of the limit
#using default 5 stone limit
print("Stone limit is {}:".format(Stone.getLimit()))
stone_objects = [Stone(name) for name in stone_names]
print("-" * 40)

#using 10 stone limit
Stone.setLimit(10)
print("Stone limit is {}:".format(Stone.getLimit()))
stone_objects = [Stone(name) for name in stone_names]
print("-" * 40)

#using 3 stone limit
Stone.setLimit(3)
print("Stone limit is {}:".format(Stone.getLimit()))
stone_objects = [Stone(name) for name in stone_names]
print("-" * 40)

#using 1 stone limit
Stone.setLimit(1)
print("Stone limit is {}:".format(Stone.getLimit()))
stone_objects = [Stone(name) for name in stone_names]
print("-" * 40)

#using 0 stone limit
Stone.setLimit(0)
print("Stone limit is {}:".format(Stone.getLimit()))
stone_objects = [Stone(name) for name in stone_names]
print("-" * 40)
