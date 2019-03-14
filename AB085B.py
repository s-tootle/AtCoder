# coding: utf-8

numN = int(input())

listd = []
for i in range(numN):
    d = int(input())
    listd.append(d)

# print(listd)
mochi = list(set(listd))
print(len(mochi))