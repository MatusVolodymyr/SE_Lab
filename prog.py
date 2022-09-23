import math
num = ((((1 + math.sqrt(5))/2)**1)-(((1 - math.sqrt(5))/2)**1))/math.sqrt(5)
for counter in range(10):
    num = ((((1 + math.sqrt(5))/2)**counter)-(((1 - math.sqrt(5))/2)**counter))/math.sqrt(5)
    print(round(num))