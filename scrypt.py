#!/usr/bin/env python3

value = "adroit#a3#vroom#b52#colorant#e111"
splited = value.split("#")         
                      
for i in splited:
    if i[-1].isdigit():
        print(i)
         