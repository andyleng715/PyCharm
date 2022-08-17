name_a_list = ["bill", "mary", "john"]
name_b_list = ["陳水扁", "蔡英文", "馬客斯", "郭台銘", "蔡英文"]

# 新增列表
name_a_list.append("Nola")
print(name_a_list)

name_a_list.append(name_b_list)
print(name_a_list)

# name_a_list.extend("Kai") #將要加入的元素用迭代的方式逐一加到列表中
# print(name_a_list)  #['bill', 'mary', 'john', 'Nola', ['王永慶', '馬客斯', '郭台銘'], 'K', 'a', 'i']

lista = [0, 1, 2, 3]
lista.insert(1, "hello")  # 把hello插入到 1 的位置
print(lista)

# 刪除列表
name_a_list.pop()  # 刪除最後一個元素
print(name_a_list)

del name_a_list[2]  # 刪除指定位數的資料
print(name_a_list)

name_b_list.remove("蔡英文")  # remove只會刪調list中的第一個，若要全刪，可以用迭代的方式
print(name_b_list)

# 修改
name_b_list[1] = "馬斯克"
print(name_b_list)

# 查找
listq = [9, 4, "fd", "h", 5, "h", "j", "y", "book", "X", "Z"]
print(5 in listq)  # 找到true 找不到false

print(listq.index("h", 1, 8))  # 在位置1~8中找h，找到的話傳回h的位置，找不到就報錯，兩個以上就傳回第一個
print(listq)

# 排序 sort
listx = [25, 3, 5, 1, 7, 13, 0]
# print("#list中有不同類型的排序 sort不會跳錯，但是會變空白")
# print("在VS Code跑會跳這個錯誤 TypeError: '<' not supported between instances of 'str' and 'int'")
# listq.sort()
# print(listq)

print("#list中同類型的排序")
listx.sort()
print(listx)
listx.reverse()
print(listx)

# 有幾個 count
listc = [1, 2, 2, 5, 1, 2, 4, 5, 3]
cnt = listc.count(2)
print(f"{listc}有幾個2 =>{str(cnt)}")