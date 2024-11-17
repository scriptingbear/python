



#define dictionaries to be stored in shelves
locations = {0: {"desc": "You are sitting in front of a computer learning Python",
                 "exits": {},
                 "namedExits": {}},
             1: {"desc": "You are standing at the end of a road before a small brick building",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "You are at the top of a hill",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5}},
             3: {"desc": "You are inside a building, a well house for a small stream",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1}},
             4: {"desc": "You are in a valley beside a stream",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2}},
             5: {"desc": "You are in the forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"2": 2, "1": 1}}
             }

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}

import os, shelve

#set working directory
os.chdir(r'C:\Users\...\My Python Scripts')

#only have to shelve 2 dictionaries here
#but what if there were 10 or 100 dictionaries that needed
#to be shelved?
#use a scalable and flexible approach by
#storing references to global dicts in a list
dict_list = [locations, vocabulary]


#create a SINGLE shelve object to store all dictionaries

#to get the name of the dictionary without knowing its
#name in advance (i.e. don't hard code the names),
#use a hack with globals() dictionary

#store a copy of globals() in a temp variable because
#iterating through it directly will fail with a
#RuntimeError: dictionary changed size during iteration

temp_globals = globals().copy() #"frozen" copy of globals()

#now use JUST ONE FILE to store both (or however many we want)
#dictionaries!

with shelve.open('game_data') as shelve_data:
    for item in dict_list:
        for k, v in temp_globals.items():
            '''
            #find the value in the globals() dictionary that matches
            #the value of an item in dict_list
            #not a good strategy for primitives like ints, however,
​            #unless each primitive has a different value'''
            
            if v == item:
                #now we know the name of the dict as a string
                dict_name = k
                #--------------original approach in challenge specification-----------#
                #the shelve file will have the name of the dictionary object
                #in dict_list that's being accessed
                #key of first (and only) entry in shelve_data file
                #will be the same as the name of the dictionary (e.g. locations), which
                #is also the name of the file
                #filename: locations[.dat|.bak|.dir] on Windows
                #first item is shelve_data['locations']
                #name of dictionary: locations
                #--------------------------new approach--------------------------------#
                #that's too confusing!
                #why not use ONE shelve with TWO entries, one for each dictionary?
                shelve_data[dict_name] = v
                #done with this iteration through globals
                #now find the name of the next item in dict_list
                break

            

#now print the shelve file
with shelve.open('game_data') as shelve_data:
    for k, v in shelve_data.items():
        print('shelve_data[{}] = {}'.format(k, v))
   
    #test to ensure you can access each dictionary in the shelve object
    #using its literal name
    #print(shelve_data['locations'])
    #print(shelve_data['vocabulary'])
    #(it works!)
