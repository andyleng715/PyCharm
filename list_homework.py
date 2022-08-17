"""
把學生隨機分到三個教室的練習
要求: 運用亂數和list，打印出分配的結果
"""
import random as r

classroom = [[], [], []] #宣告空教室
student = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"] #宣告學生list

for s in student:
    classroom_no = r.randint(0, 2)  # 從0~2的亂數(因為有3間教室，所以用0~2)，這邊的2是閉端
    classroom[classroom_no].append(s)
    print(f"第{str(classroom_no)}間教室的學生: {classroom[classroom_no]}")

i = 0  # 用以計算第幾間教室
for r in classroom:
    i += 1
    print(f"第{str(i)}間教室分配如下{r}，共有:{len(r)} 人")
    print("-" * 20)

# print(f"分配結果=>{classroom[0]}，{classroom[1]},{classroom[2]}")
