"""
 定義一個學生class
 1.必須包含姓名、學號
 2.需有國英數三科，必要時能增加科目和分數
 3.能列印學生的所有成績
"""
class Student:
    def __init__(self, name, no):
        self.name = name
        self.no = no
        self.grade = {"國文": 0, "英文": 0, "數學": 0}  # initial grade zero

    def set_grade(self, course, grade):
        if (course in self.grade) and (type(course) == str) and (type(grade) in [float, int]):
            self.grade[course] = grade
        elif (course not in self.grade) and (type(course) == str) and (type(grade) in [float, int]):
            self.grade.setdefault(course, grade)
        else:
            print("輸入格式有誤，課程(str)、分數(float)")

    def print_grade(self):
        print(f"學生:{self.name}，學號:{self.no}的成績如下:")
        for x in self.grade:  # 這邊的X是迴圈的遞增 也是會去字典中巡訪Key值並顯示出來
            print(x + "  " + str(self.grade[x]))


s1 = Student("張三", "840301")
s2 = Student("李四", "841022")

s1.set_grade("國文", 100)
s1.set_grade("物理", 97.5)

s2.set_grade("國文", 98)
s2.set_grade("數學", 100)
# print(f"學生:{s1.name}  ，成績{s1.grade}")

s1.print_grade()
s2.print_grade()
