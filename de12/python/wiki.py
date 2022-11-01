from json import tool
from sympy import python
import wikipedia

# キーワードを設定
keyword = "犬"
# キーワードで検索
wikipedia.set_lang("ja")
result = wikipedia.search(keyword)
print("検索結果",result)

print("最初の検索結果を表示")
page_data = wikipedia.page(result[0])
print(page_data.content)

from cv2 import * 
from numpy import array, where, ones_like
from matplotlib import pyplot
 
 
## カラーで読み込んだ画像をcvtColorを用いてhsvに変更 ##
img_cl = imread('tapioca_drink.png', 6)
img_hsv = cvtColor(img_cl, COLOR_BGR2HSV)
 
## 赤色の範囲を定義 ##
hsv_min = array([150,  64,   0])
hsv_max = array([180, 255, 255])
 
## 赤色をマスクする ##   
mask = inRange(img_hsv, hsv_min, hsv_max)
mask = bitwise_not(mask)
img_hsv = bitwise_and(img_hsv, img_hsv, mask = mask)
 
## 背景の黒い部分などを白くする ##
img_hsv[:, :, 2] = where(img_hsv[:, :, 2] < 10, 255 * ones_like(img_hsv[:, :, 2]), img_hsv[:, :, 2])
 
## HSVからBGRを経由して白黒に変更する ##
img_bgr = cvtColor(img_hsv, COLOR_HSV2BGR)
img_bw  = cvtColor(img_bgr, COLOR_BGR2GRAY)
 
## ごみを取るためのブラシ処理 ##
img_bw_b = blur(img_bw, (3, 3))
 
## 暗い部分のみ残してみる ##
img_bw_b = where(img_bw_b < 90, 255, 0)
pyplot.imshow(img_bw_b)