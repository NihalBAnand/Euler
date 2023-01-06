a = 1
b = 1
index = 2
while True:
    c = a + b
    index += 1
    a = b
    b = c
    if (len(str(c)) >= 1000):
        break
print(index)
