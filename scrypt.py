#!/usr/bin/env python3

value = "adroit#a3#vroom#b52#colorant#e111"
splited = value.split("#") 
vrtn = ''
                      
for i in splited:
    if not i[-1].isdigit():
        splited.remove(i)
        
print(';'.join(splited))