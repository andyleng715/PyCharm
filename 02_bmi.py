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
elif 18.5 < bmi <= 25:  # bmi > 18.5 & bmi <=25  # if條件可以用範圍表示的寫法，不用寫兩個條件
    print(str(bmi) + "_標準")
elif 25 < bmi <= 30:
    print(str(bmi) + "_偏胖")
else:
    print(str(bmi) + "_肥胖")

# --------------------------------------------------------
#用function再寫一遍
def calculate_bmi(body_height,body_weight):
    this_bmi = body_weight / ((body_height / 100) ** 2)
    if this_bmi <= 18.5:
        print(str(this_bmi) + "_偏瘦")
    elif 18.5 < this_bmi <= 25:  # bmi > 18.5 & bmi <=25  # if條件可以用範圍表示的寫法，不用寫兩個條件
        print(str(this_bmi) + "_標準")
    elif 25 < this_bmi <= 30:
        print(str(this_bmi) + "_偏胖")
    else:
        print(str(this_bmi) + "_肥胖")

    return this_bmi

body_height = float(input("身高(cm) =>"))
body_weight = float(input("體重(kg) =>"))
my_bmi = calculate_bmi(body_height,body_weight)
print(str(my_bmi))