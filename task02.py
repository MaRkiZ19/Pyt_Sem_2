"""
Дано натуральное число A > 1. 
Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
Если А не является числом Фибоначчи, выведите число -1.
Input:     5
Output:  6
"""


'''n=0
n1=1
n2=0
i=
k=int(input())
while n<=k:
    n=n1+n2
    n1,n2=n,n1
    i+=1
if (k==n2):
    print(i)
else:
    print(-1)'''


# Дано натуральное число A > 1. Определите, каким по счету числом 
# Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

# Input:     5
# Output:  6

# 1 2 3 4 5 6 7 8  9  - индексы
# 0 1 1 2 3 5 8 13 21 

"""
n0 = 0
n1 = 1
n2 = 0 - хранит сумму двух пред членов
i = 2

n2 = n0 + n1

"""

# 1 2 3 4 5 6 7 8  9  - индексы
# 0 1 1 2 3 5 8 13 21 

n = int(input())
n0 = 0
n1 = 1
n2 = 0 #- хранит сумму двух пред членов
i = 2 # - счетчик

while n2 < n:    # пока n0 < n цикл выполняется, если n0 == n - выйдем из цикла, если n0 > n - выйдем из цикла И  i = -1
    n2 = n0 + n1
    n0 = n1
    n1 = n2
    i += 1
    if n2 > n:
        i = -1
print(i)
