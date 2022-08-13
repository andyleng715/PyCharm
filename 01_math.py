"""
載入函式庫用import，python中萬物皆物件
import math as m的話 那後面使用就要 m.xxxx (as算是將物件指派成另一別名的寫法)
轉型
str()、float()、int()....
判斷型別
type(物件名)
"""
import math


"""
math.degrees(传入参数为弧度值）# 比如math.degrees(math.PI) 结果为180（度）
math.radians(传入参数为角度值）# 比如math.radians(180) 结果为PI
#角度转弧度
rad =  math.radians(角度值） #或者把知道角度的弧度值给进来：比如30度
sin(弧度)
"""
rad30 = math.radians(30)
rad60 = math.radians(60)
sin30 = math.sin(rad30)
sin60 = math.sin(rad60)
print(str(sin30) + " ; " + str(sin60))

"""
------------------------------------------------------------------
python沒有begin...end或{...} 全部用縮排表示
"""

anykey = input("請隨便輸入一個字")

if type(anykey) == str:
    print("string")
else:
    print("not string")





