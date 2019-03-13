# coding: utf-8

# コマンド入力値の取得
# numList[0] = N, numList[1] = A, numList[2] = B
numList = [int(num) for num in input().split()]
# print(numList)


totalSumPlace = 0
# N以下の数値を全探索
for i in range(numList[0]+1):
    #print("i=", i)
    place1 = i % 10         #1の位
    place10 = i // 10       #10の位
    place100 = i // 10**2   #10^2の位
    place1000 = i // 10**3  #10^3の位
    place10000 = i // 10**4 #10^4の位
    # print(place1, place10, place100, place1000, place10000)
    # 各桁の値の合計値の計算
    sumPlace = place1 + place10 + place100 + place1000 + place10000
    # print("各桁合計=", sumPlace)
    # 各桁合計値がA以上B以下であるかの判定
    if (numList[1] <= sumPlace <= numList[2] ):
        totalSumPlace += i
        #print("範囲内！")
# 合計値の出力
print(totalSumPlace)