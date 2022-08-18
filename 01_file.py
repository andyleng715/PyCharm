"""
檔案的處理
"""

import os  # rename、remove須要引用這個

f = open("text.txt", "w")  # 開檔時 W屬性若沒有找到這個檔案會自動建立一個檔案
f.close()  # open 和close 務必要成對書寫

f = open("text.txt", "w")  # 開檔時 W屬性若沒有找到這個檔案會自動建立一個檔案
for i in range(10):
    f.write(str(i) + "...hello world...\n")  # 寫入檔案
f.close()  # open 和close 務必要成對書寫

## 改名 、刪檔 (不用先open和close)
try:
    os.rename("text.txt", "test.txt")
    print("改成功")
except:
    print("改失敗")
# pass


##刪檔
try:
    os.remove("test.txt")
    print("刪成功")
except:
    print("刪失敗")
