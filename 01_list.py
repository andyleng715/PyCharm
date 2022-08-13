"""
List的應用
宣告一個空的list用來存放數據
python的list和其他語言不一樣可存放不同類型的數據資料
list用append來加入；用remove來移除
"""
num_list = []
num_list.append(987)
num_list.append("book")
num_list.append(36)
num_list.append(100)
num_list.append(78)
num_list.append(234)
num_list.append(365)
num_list.append(87)
num_list.append(135)
print("顯示list")
print(num_list)

print("移除後") #remove一定要移除存在list中的值，不然會報錯
num_list.remove("book")
print(num_list)

print("sorted(num_list) 排序後")
sorted_list = sorted(num_list)
print(sorted_list)

print("num_list.sort(reverse=True) 排序後")
print(num_list.sort(reverse=True)) #這個會顯示None
print(num_list)

print("取值")
print(num_list[0])
print(num_list[-1])  #-1表示取最後一位，也可以用下面的寫法
print(num_list[len(num_list)-1])
print("範圍取值")
print(num_list[:4]) #取第0~3 (不含4)
print(num_list[2:4])#取第2~3 (不含4)
print(num_list[3:])#取第3位後面 (含3)
print("每幾位取值")
print(num_list[::2]) #每2位取值