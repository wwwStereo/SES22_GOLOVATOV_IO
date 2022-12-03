name = input("Введите текст:")
line = 'IOEAUioeau'
s = 0
for i in name:
    if i in line:
        s = s + 1
print(s)
