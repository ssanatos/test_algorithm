
# def func_callback(input):
#     print('func_callback sum : ',input)
#     return

# def func_call(one, two, f_callback):
#     result = one + two
#     f_callback(result)
#     return

# first = 10
# second = 20

# func_call(first, second, func_callback)

def func_callback(input, extend):
    print('func_callback sum : ',input)
    print('func_callback extend sum : ',extend)
    return

def func_call(one, two, f_callback, three):
    result = one + two
    f_callback(result,three)
    return

first = 10
second = 20
third = 30

func_call(first, second, func_callback, third)