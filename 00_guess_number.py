"""
這個程式有問題，目前不能執行
"""

import random as r

count = 0
counta = 0
countb = 0
max_len = 4


# 產生幾位數的亂數
def ramdom_number(digital):
    for i in range(digital - 1):
        num_list = []
        num_list.append(r.randint(0, 9))
        num_list.append(r.randint(0, 9))
        num_list.append(r.randint(0, 9))
        num_list.append(r.randint(0, 9))

    return num_list


answer = ramdom_number(max_len)


def input_ans():
    user_ans = input(str(answer) + "輸入" + str(max_len) + "位數字，或按0看解答 => ")
    ans_list = []
    for i in range(max_len):
        ans_list.append(int(user_ans[i]))
    return ans_list


input_list = input_ans()

# print(answer)
# print(input_list)


while (input_list != answer) or (input_list != "q"):
    count = count + 1
    for x in input_list:
        if x in answer:
            if input_list.index(x) == answer.index(x):
                counta = counta + 1
            else:
                countb = countb + 1

        print(f"{input_list} = {str(counta)}A{str(countb)}B ，您猜了第 {str(count)} 次")
        input_list = input_ans()
