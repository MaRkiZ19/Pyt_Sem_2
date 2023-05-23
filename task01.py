# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 
# 0! = 1
# Решить задачу используя цикл while

# Input:       5
# 5! = 1 * 2 * 3 * 4 * 5
# Output:    120


n = int(input())
fact = 1
res = 1

while fact <= n:
    res *= fact # res = res * fact
    fact += 1
print(res)


# ------------------------------------
n = int(input())
res = 1
while n > 1:
    res *= n   # 1 * 5 4 3 2 1
    n -= 1
print(res)