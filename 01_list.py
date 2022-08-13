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
num_list.remove(36)

print(num_list)
sorted_list = num_list.sort()
print(sorted_list)
