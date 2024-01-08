def bina(arr):
    
    return len(max(''.join(list(map(str,arr))).split('0'),key=len))

print(bina([1,0,1,1]))