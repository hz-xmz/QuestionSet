import numpy as np
while True:
    try:
        str = input()
        alpha = 0
        space = 0
        number = 0
        others = 0
        for i in str:
            if i.isalpha():
                alpha += 1
            elif i.isspace():
                space += 1
            elif i.isdigit():
                number += 1
            else:
                others += 1
        print(alpha)
        print(space)
        print(number)
        print(others)
    except:
        break