#!/usr/bin/env python3

days_num = int(input("Enter a nombre: "))

if (days_num/400) == 1:
    print("Is bisextille of quatre-cent")
elif (days_num % 2) == 0:
    print("Is bisextille")
else:
    print("Is not bisextille")