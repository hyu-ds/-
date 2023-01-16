import math
color = ['black','brown','red','orange','yellow', 'green', 'blue', 'violet','grey', 'white']
value = [i for i in range(10)]
gop = [pow(10,i) for i in range(0,10)]
first_color = input()
second_color = input()
third_color = input()
for i in range(0,10):
    if first_color == color[i]:
        resistance = value[i]
for i in range(0,10):
    if second_color == color[i]:
        resistance =str(resistance) + str(value[i])
for i in range(0,10):
    if third_color == color[i]:
        resistance = int(resistance) * gop[i]
print(resistance)