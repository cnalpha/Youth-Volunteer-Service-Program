import random

# 生成一個隨機數
number = random.randint(1, 100)

# 檢查這個數字是奇數還是偶數
if number % 2 == 0:
    result = "even"
else:
    result = "odd"

# 打印結果
print(f"The generated number is {number}, which is {result}.")

01