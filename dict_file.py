psmemple = {"id": [], "name": [], "birdt": []}

f = open("psmemple.db", "w")
ans = ""

# x = f.readline()
# print(x)

def input_screen():
    print("""1.建立檔案\n2.刪除檔案\nQ.離開""")
    return input("請選擇 ==> ")


while ans not in ["q", "Q"]:
    ans = input_screen()
    if ans == "1":
        psmemple["id"].append(input("請輸入ID =>"))
        psmemple["name"].append(input("請輸入name =>"))
        psmemple["birdt"].append(input("請輸入birdt =>"))
        print(psmemple)

f.write(str(psmemple))
f.close()

