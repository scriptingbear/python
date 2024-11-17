'''
Implement a group_by_owners function that:

Accepts a dictionary containing the file owner name for each file name.
Returns a dictionary containing a list of file names for each owner name,
in any order.
For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan',
'Output.txt': 'Randy'} the group_by_owners function should return
{'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.


'''


class FileOwners:

    @staticmethod
    def group_by_owners(files):
        #get unique list of owners
        owners = set(files.values())
        #get list of files
        filenames = list(files.keys())
        result = {}
        owned_files = []
        for k,v in files.items():
            if not v in result:
                result[v] = [k]
            else:
                result[v].append(k)
        return result
            
        
#test data
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))

#with my own data
data = {'file1.txt': 'Bob', 'file2.dat': 'George', 'file3.csv': \
        'Mary', 'file4.doc': 'Larry', 'file5.ppt': 'Bob', 'file6.mdb': \
        'Mary', 'file9.txt': 'Frank', 'file10.yyz': 'George'}

print(FileOwners.group_by_owners(data))

'''
=======================================OUTPUT========================================
{'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}

{'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}
{'Bob': ['file1.txt', 'file5.ppt'], 'George': ['file2.dat', 'file10.yyz'], 'Mary': ['file3.csv', 'file6.mdb'], 'Larry': ['file4.doc'], 'Frank': ['file9.txt']}

'''

