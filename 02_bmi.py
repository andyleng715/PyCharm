"""
python沒有begin...end或{...} 全部用縮排表示
if語句的用法 if、else、elif條件式後面用:
if條件可以用範圍表示的寫法，不用寫兩個條件
"""
body_height = float(input("身高(cm) =>"))
body_weight = float(input("體重(kg) =>"))

bmi = body_weight / ((body_height / 100) ** 2)

if bmi <= 18.5:
    print(str(bmi) + "_偏瘦")
elif 18.5 < bmi <= 25:
    print(str(bmi) + "_標準")
elif 25 < bmi <= 30:
    print(str(bmi) + "_偏胖")
else:
    print(str(bmi) + "_肥胖")

# --------------------------------------------------------

a = 10
if a > 0 & a <= 10:  # if條件可以用範圍表示的寫法，不用寫兩個條件
    print("x")
else:
    print("O")
