import math


def get_func(ls):
    function_list = []
    for item in ls:
        if item == 'square':
            function_list.append(lambda x: x**2)
        elif item == 'circle':
            function_list.append(lambda r: math.pi*(r**2))
        elif item == 'rectangle':
            function_list.append(lambda x, y: x*y)
        else:
            function_list.append(lambda h, g: (g*h)/2)
    return function_list


ls = get_func(['square', 'circle', 'rectangle', 'triangle'])
