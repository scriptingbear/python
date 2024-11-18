def nestify(flat_list, sublist_size):
  #Validate input
  if len(flat_list) == 0:
    return []
  if sublist_size < 1:
    return []
  
  #Need the last index of the source list
  #when configuring the range() object so
  #we know when to stop iterating
  last_index = len(flat_list) - 1 #lists are 0 based

  #Create an empty list to hold the 
  #sublists
  nested_list = []

  #Slice through the source lists in increments of
  #the specified sublist size, generating sublists
  #to append to the nested list

  for current_index in range(0, last_index, sublist_size):
    sublist = flat_list[current_index : current_index + sublist_size]
    nested_list.append(sublist)
  
  return nested_list