#!/usr/bin/env python3

def count(string):    
    dic = {
            'a': int(0),
            'e': int(0),
            'i': int(0),
            'o': int(0),
            'u': int(0),
            'y': int(0),
    }
        
    for char in string:
        if char in dic.keys():
            dic[char] += 1;
            
    return dic

dic = count(input("Enter a sentence to analyze: "))


for i in dic:
    print("Character {0}: {1}".format(i, dic[i]))