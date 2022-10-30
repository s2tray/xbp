import random
a = random.randint(1, 100)
print(a)
# 解答者が爆弾を回避する

suji_list=[] #suji_listというリストを作る
for i in range(1,100):
    print(i)

    suji_list.append(suji_list) #ここでsujiという変数の値をリストに追加している

import random

answer = random.randint(1, 100)
turn = 0

print('★ 数当てゲーム ★')

while True:

    n = int(input('1~100 の間の数字を入力してください: '))

    turn += 1

    if n < answer:
        print('もっとビック')

    elif n > answer:
      print('もっとスモール')

    else:
      print('正解!!')
      break

print('答えは {}, 正解までに {} ターンかかりました'.format(answer, turn))


start_time = time.perf_counter ()
"""コード"""
end_time = time.perf_counter ()

# 計測した時間の計算(秒数)
tim = end_time - start_time
# 秒数から分数のみ(秒数なし)を計算
mint = tim // 60
# 秒数から秒数のみ(分数なし)を計算
secd = (tim % 60) - mint
# 分数は小数点以下を非表示(計算の時点で必ず0のため)、秒数は小数点第一位まで表示
print ( "所要時間は {:.0f} 分 {:.1f} 秒".format ( mint, secd ) )