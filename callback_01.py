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

if __name__ == '__main__':
   try:
        f = open('./testfile.txt','r')
        length = len(f.read())
        f.close()
        print(length)
   except Exception as e:
        pass
