# 6. Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

_list= ['krishan', 'john', 'bikalpa', 'sanjaya', 'sita', 'suman']

for items in _list:
    flag= 0
    if items=='john':
        print("the item is in index ", _list.index("john"))
        flag= 1
        break
if flag==0:
    print("not found")