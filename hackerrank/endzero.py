def endnum(arr):
    for en in arr:
        if en==0:
            arr.remove(en)
            arr.append(en)
    return arr

print(endnum([0,1,0,3,12]))