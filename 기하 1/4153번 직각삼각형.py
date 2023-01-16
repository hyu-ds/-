import math
import sys
zero = False
will_print_it = []
while zero == False:
    a, b, c = map(int, sys.stdin.readline().split())
    a_sq = math.pow(a,2)
    b_sq = math.pow(b,2)
    c_sq = math.pow(c,2)
    if a == 0:
        zero = True
    else:
        if a_sq == b_sq + c_sq or b_sq == a_sq + c_sq or c_sq == a_sq + b_sq:
            will_print_it.append('right')
        else:
            will_print_it.append('wrong')
for i in will_print_it:
    print(i)