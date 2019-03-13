# 標準入力の数値を取得
# rangeで数値配列を作成すると数値が足りないので１を足す
# 例えば、range(3)だと、[0,1,2]となり3がないので、[0,1,2,3]を作りたいならrange(4)にする
coin500 = int(input()) + 1
coin100 = int(input()) + 1
coin50 = int(input()) + 1
totalX = int(input())

# カウント用変数numCombinationの初期化
numCombination = 0

#500円硬貨、100円硬貨、50円硬貨の組み合わせを全探索
#(i=1,j=1,K=1)の組み合わせの合計値がXと等しいかを比較 
#次に(i=1,j=1,K=2)、(i=1,j=1,K=3)、・・・、(i=1,j=1,K=coin50)と50円硬貨の枚数を変化させてXと比較する
#Kが一巡したら、j=2として、再度(i=1,j=2,K=1)、(i=1,j=1,K=2)、・・・、(i=1,j=2,K=coin50)と50円硬貨の枚数を変化させてXと比較する
#これをiも同様に変化させる
for i in range(coin500):
    totalCoin500 = 500 *  i
    for j in range(coin100):
        totalCoin100 = 100 * j
       for k in range(coin50):
            totalCoint50 = 50 * k
            totalAmount = totalCoin500 + totalCoin100 + totalCoint50
            # print(totalAmount, "i=", i, "j=", j, "k=", k)
# 計算値とXが一致した回数をカウント
            if (totalAmount == totalX):
                numCombination += 1
#結果の出力
print(numCombination)