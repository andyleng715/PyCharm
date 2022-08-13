"""
單雙引號都可以，但一定要成對
print中 ,和+都可字串相加，但,號可以加文字和數字的  +號只可以是文字加文字
\表示後面跟著的是"文字"
\n表示換行

註解單行 # ，多行用三個"
"""

#字串太長可以用+相連
str = "Hello "+ "world"
print(str)

#字串太長可以用\相連換行書寫(注意頭尾的"，還有換行後是從"頭"開始，不要縮排，縮排會當成是空白)
str = "Hello \
world "
print(str)


print("x", 456)
print("hello" + " world")
print("let's go")
print("let\'s go")
print("let's \n go")
print("這是第一行\n")
print("這是第二行\n")
print("這是第三行\n")
