num = int(input())
origin_num = num
new_num = -1
cycle = 0
while new_num != origin_num :
    if num < 10:
        new_num = num*10+num
        cycle += 1
        num = new_num

    else:
        new_num = (num % 10) * 10 + (((num % 10) + (num//10)) % 10)
        cycle += 1
        num = new_num
print(cycle)