# 첫번째 근위병
num = 1000
doors = [True]*num

for guard in range(2,num+1):
    for i, d in enumerate(doors):    
        if (i+1) % guard == 0:
            if d == True:
                doors[i] = False
            elif d == False:
                doors[i] = True
open_doors = [i+1 for i, d in enumerate(doors) if d]
count = len(open_doors)
print(f'{count}\n{open_doors}')