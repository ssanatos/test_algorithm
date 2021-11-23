a = 10
b = 0

try:
    c = a/b
except ZeroDivisionError:
    c = a/1

print(c)