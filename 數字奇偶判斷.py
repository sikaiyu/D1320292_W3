a=int(input("請輸入整數:"))
result = "偶數" * (a % 2 == 0) + "奇數" * (a% 2 != 0)
print("結果:",a,"是",result)