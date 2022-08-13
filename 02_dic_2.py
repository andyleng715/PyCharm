"""
https://selflearningsuccess.com/python-dictionary/
字典檔的其他使用，搭配loop

range(begin, end ,step)
begin為起始數，end為終止數(不等於)  **python的終止數似乎都不等於  比如 str[2:5] 就是str中第2到第4的文字
step default = 1，即每次增加的步長

"""

score_dict ={"兄大":85,
             "老二":30,
             "張三":87,
             "李四":64,
             "王五":72,
             "華六":99,
             "吳七":48,
             "王八":58,
             "趙九":32,
             "陳十":59
             }
dict(Muffin=39, Scone=25, Biscuit=20)
#重新指派原本的key表示更新字典檔內的值(老師偷把陳十的分數改為60分)
score_dict["陳十"] = "60"

#若傳入的key存在就傳回原本的key值，否則會新增一筆資料
score_dict.setdefault("王八",100)
score_dict.setdefault("mary",77)

#顯示所有的keys
print(score_dict.keys())
#顯示所有的values
print(score_dict.values())
#顯示所有的items
print(score_dict.items())
print(score_dict)


print("誰考不及格")
for score_tuple in score_dict.items():
    student_name = score_tuple[0]
    student_score = score_tuple[1]
    if student_score < 60:
       print(student_name + ":" + str(student_score))

#若想要輸出不及格的人，並用分數(value)來排序，該怎麼做呢?