i = 37 
while(True):
    if i % 13 == 2 and i % 37 == 2:
        if i > 80000:
            if str(i)[-1] == '9':
                print(i)
                break
    i += 1