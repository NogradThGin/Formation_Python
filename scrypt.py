#!/usr/bin/env python3

def line_count():  
    count = int(0)
    
    file = open('./example_file', 'r')
    for i in file.readlines():
        count += 1
    
    file.close()    
    return count

def word_count():  
    count = int(0)
    
    file = open('./example_file', 'r')
    for i in file.readlines():
        count += len(i.split())
    
    file.close()
    return count
    
print("There is {0} lines".format(line_count()))
print("There is {0} words".format(word_count()))