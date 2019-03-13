# coding: utf-8

numCard = int( input() )
cardList = [int(num) for num in input().split()]

cardList.sort(reverse=True)
#print(cardList)

sumAlice = 0
sumBob = 0
for i in range(numCard):
    if (i % 2 == 0):
        sumAlice += cardList[i]
    else:
        sumBob += cardList[i]
scoreDifference = sumAlice - sumBob
#print(sumAlice)
#print(sumBob)
print(scoreDifference)
