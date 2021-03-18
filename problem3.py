# class word(object):
#     def __init__(self,string,index):
#         self.string=string
#         self.index=index
#     def create_dup_array(string,size):
#         dup_array=[]
from collections import defaultdict 
 
def printAnagramsTogether(words):
    groupedWords = defaultdict(list)
 
    for word in words:
        groupedWords["".join(sorted(word))].append(word)
 
    for group in groupedWords.values():
        print(" ".join(group))      
 
 
if __name__ == "__main__":   
    arr =  ["cat", "dog", "tac", "god", "act"]  
    printAnagramsTogether(arr) 
