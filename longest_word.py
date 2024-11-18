def LongestWord(sen): 

    # code goes here 
    import re
    if not sen:
        return ''
    elif not re.compile(r'[a-z]+').search():
    if sen:
        #strip out non alphabetic characters, preserving spaces
        regex = re.compile(r'[^a-z ]', re.I)
        sen = regex.sub('', sen)
    
        #split into list so each word's length can be determined
        words = sen.split()
        
        #generate list of word lengths
        word_len = [len(word) for word in words]
        
        #obtain maximum word length
        max_word_len = max(word_len)
        
        #locate element in word_len corresponding to index of maximum word length
        max_word_index = word_len.index(max_word_len)
        
        #return longest word in sen
        sen = words[max_word_index]
        
        return sen
    else:
        return ''
    
