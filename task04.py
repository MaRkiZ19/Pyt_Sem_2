# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: 
# один для себя, а другой для тещи. Понятно, что для себя нужно выбрать 
# арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком 
# много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Далее 
# N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input:	5 -> 5 1 6 5 9
# Output:	1 9

n = int(input())
kg =  int(input())
max1 = kg
min1 = kg

for i in range(n - 1):
    kg =  int(input())
    if kg < min1:
        min1 = kg
    if kg > max1:
        max1 = kg
print(min1, max1)
