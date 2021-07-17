file = open('text.txt','w') 
file.write("This is the write command and the command is written by sushanth and Tejas\n") 
file.write("It allows us to write in a particular file")
file.close()
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count('text.txt'))
