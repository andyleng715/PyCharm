"""
同樣是assign，不同類型，意義不同
"""
list_x = []
list_x.append(5)
list_x.append(3)
list_x.append(4)
list_x.append(7)

print("list指派，指派後list_y和list_x存在相同的記憶體位置???")
list_y = list_x
list_z = sorted(list_x)  # 這樣就不會直接存在同一個記憶體的位置(好像)
list_z.append(6666)
print(list_x)
print(list_y)
print(list_z)

print("list_y.append(365)")
list_y.append(365)
print(list_x)
print(list_y)
print(list_z)

print("sorted list_x")
list_x.sort(reverse=True)  # 反向排序
print(list_x)
print(list_y)
print(list_z)

print("以下一般的變數指派，指派後a和b可再指派不同的值")
a = 3
b = a
b = 5
print("a = "+str(a)+" ; b = "+str(b))

