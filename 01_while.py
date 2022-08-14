"""
while loop
"""


def input_function():
    input_num = input("請輸入數字計算平均數，按q離開 => ")
    return input_num


def while_test01():
    count = 0
    total = 0
    num = input_function()
    while num not in [" ", "q", "Q"]:
        total = total + float(num)
        count = count + 1
        num = input_function()

    if count == 0:
        print("輸入總和為 = 0  ，平均為 = 0")
    else:
        print("輸入總和為 = " + str(total) + " ，平均為 = " + str(total / count))


# -----------------------------------------------------------------------------------------------------------------------

def while_test02():
    count = 0
    total = 0
    input_num = input("while_test02 請輸入數字計算平均數，按q離開 => ")
    while input_num not in [" ", "q", "Q"]:
        total = total + float(input_num)
        count = count + 1
        input_num = input("while_test02 請輸入數字計算平均數，按q離開 => ")

    if count == 0:
        print("輸入總和為 = 0  ，平均為 = 0")
    else:
        print("輸入總和為 = " + str(total) + " ，平均為 = " + str(total / count))


while_test02()
