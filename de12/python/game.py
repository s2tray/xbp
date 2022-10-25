# randomをインポート
import random
# timeをインポート
import time


# 解答者が選んだ数字が大きいか、小さいか返す関数
def high_low():
    # 数字が200以内なら文言が変わる
    if (guess < secret_number) and (guess + 200 >= secret_number):
        return ("\nもう少し、大きい数字です。(200以内)")
    if (guess > secret_number) and (guess <= secret_number + 200):
        return ("\nもう少し、小さい数字です。(200以内)")
    # 数字が大きいか、小さいかの文言
    if guess < secret_number:
        return ("\nもっと、大きい数字です。")
    if guess > secret_number:
        return ("\nもっと、小さい数字です。")


# 各ヒントをまとめた関数
def hint(select):
    # 1回目で外した場合、偶数か奇数かを表示
    if guesses_taken == 1:
        print ( "\n偶数か奇数かを表示する……" )
        # 2で割り、余りがなかったら、True
        if not (secret_number % 2):
            return ("…… 偶数!!")
        # 2で割り、余りがあったら、True
        if (secret_number % 2):
            return ("…… 奇数!")

    # 2回目で外した場合、3で割れるか、5で割れるか、を表示
    if guesses_taken == 2:
        print ( "\n3で割れるか、5で割れるか、表示する……" )
        # 3で割っても5で割っても余りがない
        if not (secret_number % 3) and not (secret_number % 5):
            return ("…… 両方で割れる")
        # 3で割ったら余りがない
        if not (secret_number % 3):
            return ("…… 3で割り切れる(5で割れない)")
        # 5で割ったら余りがない
        if not (secret_number % 5):
            return ("…… 5で割り切れる(3で割れない)")
        return ("…… どちらでも割れない")

    # 3回目で外した場合、各桁の数字を表足す
    if guesses_taken == 3:
        # 答えの数字を文字列に変えて、dに格納
        # dにある文字列を、1文字ずつ数字に変えリスト化
        digits = [int ( d ) for d in str ( secret_number )]
        return ("\n各桁の数字を足す……"
                "\n…… " + str ( sum ( digits ) ))  # 各数字を足して文字列型にする

    # 4回目で外した場合、下2桁目を表示
    if guesses_taken == 4:
        return ("\n下2桁目を表示する……"
                "\n…… " + str ( secret_number )[-2])  # 後ろから2文字目を取得

    # 5回目で外した場合、±10以内のランダム数字を表示
    if guesses_taken == 5:
        return ("\n±10以内の数字をランダムで表示する……"
                "\n…… " + str ( random.randint ( secret_number - 10, secret_number + 10 ) ))


# 使用したヒントを表示するための記録用、空リスト
record = []

# 0 ~ 10,000までの数字をランダムに決め、secret_numberに格納
secret_number = random.randint ( 0, 10000 )
print ( "0から10,000までの数字を当ててください。" )

# 時間の計測開始
start_time = time.perf_counter ()

# 最大6回繰り返す
for guesses_taken in range ( 1, 7 ):
    print ( "\n数字を入力してください。" )
    # 入力してもらった数字をguessに格納
    # input()は文字列を返すので、int()で整数値に変換
    guess = int ( input () )

    if guesses_taken == 6:
        break

    # 数字が当たればbreakでforループから抜け出す
    if guess == secret_number:
        break

    print ( high_low () )

    # ヒントを、順番に列挙したタプルを用意
    used_ability = ("偶数か奇数か", "3で割れるか、5で割れるか", "各桁の数字を足す", "下2桁目を表示", "±10以内の数字をランダムで表示")
    print ( "\nヒントを使いますか?\n 1:はい / 2:いいえ" )
    yesno = int ( input () )
    # yesnoが1だった場合
    if yesno == 1:
        # 解答数に応じた能力を使う
        ability = hint ( guesses_taken )
        print ( ability )
        # 能力のタプルから、解答回数に応じた能力名を、onebyoneに格納
        onebyone = used_ability[guesses_taken - 1]
        # 順番にrecord = []に格納にしてリスト化
        record.append ( onebyone )
    # yesnoが1以外だった場合pass
    if not yesno == 1:
        pass

# 時間の計測終了
end_time = time.perf_counter ()

# 当たった場合とハズレた場合で文言を変える
if guess == secret_number:
    print ( "\nグッド! " + str ( '{:,}'.format ( guesses_taken ) ) + "回で当たり!" )
if guess != secret_number:
    print ( "\n結果だけを求めていると、人は近道をしたがるものだ……………"
            "\n近道した時、真実を見失うかもしれない"
            "\nやる気もしだいに失せていく"
            "\n大切なのは『真実に向かおうとする意志』だと思っている"
            "\n……正解は " + str ( '{:,}'.format ( secret_number ) ) )

# 使用したヒントを表示
print ( "\n使用したヒント" )
print ( record )

# 計測した時間の計算(秒数)
tim = end_time - start_time
# 秒数から分数のみ(秒数なし)を計算
mint = tim // 60
# 秒数から秒数のみ(分数なし)を計算
secd = (tim % 60) - mint
# 分数は小数点以下を非表示(計算の時点で必ず0のため)、秒数は小数点第一位まで表示
print ( "所要時間は {:.0f} 分 {:.1f} 秒".format ( mint, secd ) )