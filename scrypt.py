#!/usr/bin/env python3

def line_count():  
    count = int(0)
    
    file = open('./example_file', 'r')
    
    for i in file:
        count += 1
        
    return count

def word_count():  
    count = int(0)
    
    file = open('./example_file', 'r')
    for i in file.readlines():
        if(i != '\n'):
            #print(len(i.split()))
            count += len(i.split())
    
    return count
    
print(word_count())